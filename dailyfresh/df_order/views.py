#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render,redirect
from df_user import user_decorator
from df_user.models import UserInfo
from df_cart.models import *
from plc_store.models import *

from django.db import transaction
from .models import *
from datetime import datetime
from decimal import Decimal

import snap7.client as c
from snap7.util import *
from snap7.snap7types import *

@user_decorator.login
def order(request):
    #查询用户对象
    user=UserInfo.objects.get(id=request.session['user_id'])
    #根据提交查询购物车信息
    get=request.GET
    cart_ids=get.getlist('cart_id')
    cart_ids1=[int(item) for item in cart_ids]
    carts=CartInfo.objects.filter(id__in=cart_ids1)
    #构造传递到模板中的数据
    context={'title':'提交订单',
             'page_name':1,
             'carts':carts,
             'user':user,
             'cart_ids':','.join(cart_ids)}
    return render(request,'df_order/order.html',context)

'''
事务：一旦操作失败则全部回退
1、创建订单对象
2、判断商品的库存
3、创建详单对象
4、修改商品库存
5、删除购物车
'''

@transaction.atomic()
@user_decorator.login
def order_handle(request):
    tran_id=transaction.savepoint()
    #接收购物车编号
    cart_ids=request.POST.get('cart_ids')#5,6
    try:
        #创建订单对象
        order=OrderInfo()
        now=datetime.now()
        uid=request.session['user_id']
        order.oid='%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
        order.user_id=uid
        # print order.oid
        order.odate=now
        order.oaddress=request.POST.get('address')
        order.ototal=0
        order.save()
        #创建详单对象
        cart_ids1=[int(item) for item in cart_ids.split(',')]
        total=0
        for id1 in cart_ids1:
            detail=OrderDetailInfo()
            detail.order=order
            # 查询购物车信息
            cart=CartInfo.objects.get(id=id1)
            # 判断商品库存
            goods=cart.goods
            if goods.gkucun>=cart.count:#如果库存大于购买数量
                # 减少商品库存
                goods.gkucun=cart.goods.gkucun-cart.count
                goods.save()
                # 完善详单信息
                detail.goods_id=goods.id
                price=goods.gprice
                detail.price=price
                count=cart.count
                detail.count=count
                detail.save()
                total=total+price*count
                #删除购物车数据
                cart.delete()
            else:#如果库存小于购买数量
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart/')
                # return HttpResponse('no')
        # 保存总价
        order.ototal=total+10
        order.save()
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print ('================%s'%e)
        transaction.savepoint_rollback(tran_id)

    # return HttpResponse('ok')
    return redirect('/user/order/')


@user_decorator.login
def pay(request,oid):
    order=OrderInfo.objects.get(oid=oid)
    order.oIsPay=True
    order.save()
    context={'order':order}
    try:
        #连接PLC
        plc=c.Client()
        plc.connect('192.168.18.17',0,2)
        #获取V区域数据
        writePLCstore(plc,'100',1,S7WLBit,1)#向V100.0，表示出库；
        
        position=StoreInfo.objects()#实例化库位模型对象
        p=position.aggregate(Min('times')).filter(isPossess=1)#选择时间最短，有货的库位
        #判断订单是金属还是塑料
        if order.types()==1:
            X=1
        elif order.types()==2:
            X=2
        Y=P.slie
        Z=P.sceng
        writePLCstore(plc,'101',0,S7WLByte,X)#分配出库排号；
        writePLCstore(plc,'102',0,S7WLByte,Y)#分配出库列号；
        writePLCstore(plc,'103',0,S7WLByte,Z)#分配出库层号；
        # 断开连接
        client.disconnect()
        client.destroy()
    except:
        pass
    return render(request,'df_order/pay.html',context)
    
def writePLCstore(plc,byte,bit,dataLength,value):
    result = plc.read_area(0x87, 0, byte, dataLength)
    if dataLength == S7WLBit:
        set_bool(result,0,bit,value)
    elif dataLength == S7WLByte or dataLength == S7WLWord:
        set_int(result,0,value)
    elif dataLength == S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(0x87, 0, byte,result)
    
    
    
