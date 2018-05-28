#连接PLC
plc=c.Client()
plc.connect('192.168.18.17',0,2)
#获取V区域数据

while True:
   VB100_1=readPLCstore(plc,'100',1,S7WLBit,1)#读取VB100.1；
   if VB100_1==1:#入库
        X=readPLCstore(plc,'100',0,S7WLByte,1)#读取V99的值；
        Z=P.sceng
        writePLCstore(plc,'101',0,S7WLByte,X)#分配出库排号；
        writePLCstore(plc,'102',0,S7WLByte,Y)#分配出库列号；
        writePLCstore(plc,'103',0,S7WLByte,Z)#分配出库层号；
    
def readPLCstore(plc,byte,bit,dataLength):
    result = plc.read_area(0x87, 0, byte, dataLength)
    if dataLength == S7WLBit:
        set_bool(result,0,bit,value)
    elif dataLength == S7WLByte or dataLength == S7WLWord:
        set_int(result,0,value)
    elif dataLength == S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(0x87, 0, byte,result)
    
def writePLCstore(plc,byte,bit,dataLength,value):
    result = plc.read_area(0x87, 0, byte, dataLength)
    if dataLength == S7WLBit:
        set_bool(result,0,bit,value)
    elif dataLength == S7WLByte or dataLength == S7WLWord:
        set_int(result,0,value)
    elif dataLength == S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(0x87, 0, byte,result)