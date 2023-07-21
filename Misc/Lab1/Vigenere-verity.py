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
    
key=Text_List.index('.')
p=(Text_List.index('9')*inverse(key,97))%97
print(Text_List[p])