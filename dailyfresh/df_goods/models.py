# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    ttitle=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    class Meta:
        verbose_name = '类型'
        verbose_name_plural = verbose_name
        ordering = ['id']
    def __str__(self):
        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle=models.CharField(verbose_name="名称",max_length=20)
    gpic=models.ImageField(upload_to='goods')
    gprice=models.DecimalField(verbose_name="单价",max_digits=5,decimal_places=2)
    isDelete=models.BooleanField(default=False)
    gunit=models.CharField(verbose_name="单位",max_length=20,default='500g')
    gclick=models.IntegerField(verbose_name="点击量",)
    gjianjie=models.CharField(max_length=200)
    gkucun=models.IntegerField(verbose_name="库存",)
    gcontent=HTMLField()
    gtype=models.ForeignKey(TypeInfo,verbose_name="类型",)
    # gadv=models.BooleanField(default=False)
    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name
        ordering = ['id']
    def __str__(self):
        return self.gtitle.encode('utf-8')
