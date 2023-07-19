#VIgenere-decrypt1 use for get the length of key
from random import randrange

text_list=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'
#key 是从text_list中随机选择15-30个的字符 生成的密钥
def TextRead(file):
     #将txt文件转化为字符串
    with open(file,"r") as f :
        TextContent = f.read()
    return TextContent 

def Num(s):
    #已经是分组之后取出的一组字符串 ，计算单组中的重合指数   
    count=[0]*97
    Num = 0 
    for i in range(len(s)):
        index=text_list.index(s[i])
        count[index]+=1
    for i in range(97):
        if count[i]!=0:
            Num+=count[i]*(count[i]-1)
    Num/=len(s)*(len(s)-1)    
    return Num

def Ic(s,k):
    #用来统计不同k值下的重合指数
    Ic=[]
    str=""
    for i in range(len(s)//k):#组数
          for x in range(i,len(s),k):
            str+=s[x]
          p = Num(str)
          Ic.append(p)
    return Ic

T=TextRead("vigenere.txt")

for k in range(15,31):
    p=0 #p用于改变存放每个k值下的Ic值总合
    for x in range(k):
        p+=Ic(T,k)[x]
    p/=k
    print (p)
#C[i]中存放的是Ic的均值
    
