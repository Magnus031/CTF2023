key=[0]*24
key1=[0xEC,0x10,0x94,0x6C,0XE3,0X12,0X2B,0X67,0X62,0X68,0X90,0X2B,0X7E,0X30,0XEE,0XE6,0X49,0XEC,0XA4,0X52,0XF3,0X7C,0X78,0XCA]
key2=[0xFB,0X61,0X7,0X84,0XE2,0X52,0XB0,0XF7,0XF7,0X70,0X5E,0X69,0XBE,0XB5,0XE8,0XA5,0X58,0XCB,0XFB,0XF2,0X8D,0X2E,0X85,0XE]
for x in range(24):
    key[x]=key1[x]^key2[x]
print(key)