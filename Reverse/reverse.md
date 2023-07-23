# Reverse Lab1:Baby Reverse
## 3220102732-周伟战
### Task1
#### 1.1 Part 1
> 先利用zsh中的readelf -h practice命令行得到入口地址为0x1443
可以看到这个运行的是start()函数

![P7](https://github.com/Magnus031/CTF2023/blob/main/Reverse/P7.png?raw=true)
##### 1.1.1在题目中有一个函数是加密相关的函数，请找出这个函数的地址（Hex 格式作答，5 points）
![P1](https://github.com/Magnus031/CTF2023/blob/main/Reverse/P1.png?raw=true)
> 这里将result,a1,a3的类型都变成了_BYTE*类型(a3是一个指针数组)，,更改这些变量的类型之后发现已经有些C语言雏形了。
这个加密算法其实是RC4加密算法，下面这个P2更能验证这个加密算法是RC4
Line20的^ XOR运算就能大概知道这是加密算法
(Sub_11DF)

![P3](https://github.com/Magnus031/CTF2023/blob/main/Reverse/P3.png?raw=true)
> 从左边的导航栏可以看见，这个加密函数的地址是00000000000011DF	

##### 1.1.2当你找到了这个加密函数，请找出程序在加密过程中所使用到的密钥 （5 points）
观察start()函数，可以知道密钥是'uwin@aaa'
##### 1.1.3在这个题目中，程序简单封装了短字符串类型，请在 IDA 中恢复它的结构体 （截图或用 C 语言表示该结构， 15 points）
![P4](https://github.com/Magnus031/CTF2023/blob/main/Reverse/P4.png?raw=true)
> 将sub_13C6函数输入的类型改成_int64，发现write函数中偏移+4的位置，推断得出，封装的字符类型string中前4个字节代表长度，后面3*8=24字节是拿来放string的内容；
如int v6,__int64 v7[3]就是这样4+3 * 8字节
##### 1.1.4给出你解答的 flag 内容及 Writeup （15 points）
> RC4加密算法和解密算法的密钥是同一个

>  Step1我们获得了密钥是'aaa@niwu'
Step2 由1.1.3中可以得知，我们把string的结构体分析出来了，是4字节带上3*8字节，需要解密的密文是

![P8](https://github.com/Magnus031/CTF2023/blob/main/Reverse/P8.png?raw=true)
v17 v18 v19之间顺序相连，但内部是倒序相加
> 得到需要利用RC4的密文是FB610784EF0AF4DBCB755955B8DAD19F1A86

剩下我们利用cyberchef
![P9](https://github.com/Magnus031/CTF2023/blob/main/Reverse/P9.png?raw=true)
得到的flag是**AAA{y0u_c4tch_Me!}**
#### 1.2 Part 2
![P10](https://github.com/Magnus031/CTF2023/blob/main/Reverse/P10.png?raw=true)
> 由readelf -h chall可以得到函数入口的地址是0x10e0，但进入了start()函数发现，其实看的是main函数，在了解相关的加密算法后发现`aUwinAaa`这个数组里面存放的就是密钥

##### 1.2.1程序中加密函数用到的的密钥是什么，你是如何找到它的（10 points）
![P11](https://github.com/Magnus031/CTF2023/blob/main/Reverse/P11(1).png?raw=true)
sub_151C函数是一个相对独立的函数，可以单独分析，看sub_151C函数可以发现是用来形成密钥以及获得密文的
![P12](https://github.com/Magnus031/CTF2023/blob/main/Reverse/P12.png?raw=true)
`aUwinAaa[i]`中的初值是`'uwin@aaa'`
先看`aUwinAaa[i]^=*((_BYTE *)&v4[-1] + i);`这个语句，其实是把v[3]中存放的字符串与`aUwinAaa`这个密钥数组和`ABDAD7818A9FDBDF`进行异或操作得到密钥是`0xDEADBEEFCAFEBABE`
```Python
key=[0x75,0x77,0x69,0x6e,0x40,0x61,0x61,0x61]
key2=[0xab,0xda,0xd7,0x81,0x8a,0x9f,0xdb,0xdf]
key3=[0]*8
for x in range(8):
    key3[x]=key[x]^key2[x]
print(key3)
```
（代码在 XOR.py）中
##### 1.2.2给出你解答的 flag 内容及 Writeup（20 points）
再看密文
![P13](https://github.com/Magnus031/CTF2023/blob/main/Reverse/P13.png?raw=true)
> 可以得到加高亮的那一行后面的内容就是储存在byte_4034中的初始值是：0xFB, 0x61, 0x7, 0x84, 0xE2, 0x52, 0xB0, 0xF7, 0xF7, 0x70, 0x5E, 0x69, 0xBE, 0xB5, 0xE8, 0xA5, 0x58, 0xCB, 0xFB, 0xF2, 0x8D, 0x2E, 0x85h, 0xE

> 再看v4[0],v4[1],v4[2]中分别0xEC,0x10,0x94,0x6C,0XE3,0X12,0X2B,0X67,0X62,0X68,0X90,0X2B,0X7E,0X30,0XEE,0XE6,0X49,0XEC,0XA4,0X52,0XF3,0X7C,0X78,0XCA
利用
```Python
key=[0]*24
key1=[0xEC,0x10,0x94,0x6C,0XE3,0X12,0X2B,0X67,0X62,0X68,0X90,0X2B,0X7E,0X30,0XEE,0XE6,0X49,0XEC,0XA4,0X52,0XF3,0X7C,0X78,0XCA]
key2=[0xFB,0X61,0X7,0X84,0XE2,0X52,0XB0,0XF7,0XF7,0X70,0X5E,0X69,0XBE,0XB5,0XE8,0XA5,0X58,0XCB,0XFB,0XF2,0X8D,0X2E,0X85,0XE]
for x in range(24):
    key[x]=key1[x]^key2[x]
print(key)
```
获得异或处理过后的密文（代码在p.py中）
利用cyberchef中的RC4解密,最终得到flag:**AAA{amAz1ng_y0u_F1nd_M3}**
![P14](https://github.com/Magnus031/CTF2023/blob/main/Reverse/P14.png?raw=true)
Over!

---
### Task2
看似随机却并不随机，看似模糊却又清晰，请你耐心分析并提交：
emm没太看懂题目
over!
