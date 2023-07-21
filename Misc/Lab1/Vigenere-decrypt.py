Text_List=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'
def gcd(a,b):
    #用于计算最大公因数,默认a>=b
    if b==0:
        return a 
    else:
        return  gcd(b,a%b)

def inverse(a,n):
    #用来判断a的乘法逆元是否存在，如果存在则输出
    b,y=0,0
    if gcd(n,a)==1:
        while y <=0:
            if (1-n*y) % a==0:
                b= (1-n*y)//a
                return b
            else: 
                y-=1
    else:
        return 0 
def TextRead(file):
     #将txt文件转化为字符串
    with open(file,"r") as f :
        TextContent = f.read()
    return TextContent 

key=[0]*29
Text=TextRead('vigenere.txt')
key[0]=inverse(Text_List.index('S'),97)
key[1]=inverse(Text_List.index('.'),97)
key[2]=inverse(Text_List.index('6'),97)
key[3]=inverse(Text_List.index('z'),97)
key[4]=inverse(Text_List.index('c'),97)
key[5]=inverse(Text_List.index('K'),97)
key[6]=inverse(Text_List.index('1'),97)
key[7]=inverse(Text_List.index('r'),97)
key[8]=inverse(Text_List.index('P'),97)
key[9]=inverse(Text_List.index('1'),97)
key[10]=inverse(Text_List.index('I'),97)
key[11]=inverse(Text_List.index('A'),97)
key[12]=inverse(Text_List.index('y'),97)
key[13]=inverse(Text_List.index('~'),97)
key[14]=inverse(Text_List.index('\\'),97)
key[15]=inverse(Text_List.index('p'),97)
key[16]=inverse(Text_List.index('-'),97)
key[17]=inverse(Text_List.index('h'),97)
key[18]=inverse(Text_List.index('o'),97)
key[19]=inverse(Text_List.index('2'),97)
key[20]=inverse(Text_List.index('a'),97)
key[21]=inverse(Text_List.index('R'),97)
key[22]=inverse(Text_List.index('4'),97)
key[23]=inverse(Text_List.index('&'),97)
key[24]=inverse(Text_List.index('D'),97)
key[25]=inverse(Text_List.index('G'),97)
key[26]=inverse(Text_List.index('X'),97)
key[27]=inverse(Text_List.index('\''),97)
key[28]=inverse(Text_List.index('a'),97)
Text_List=list(Text_List)
Text=list(Text)
Text1=''
for i in range(len(Text)):
    q=i%29
    if q in range(29):
        Text1+=Text_List[(Text_List.index(Text[i])*key[q])%97]
    else:
        Text1+=Text[i]
print (Text1)
    
        