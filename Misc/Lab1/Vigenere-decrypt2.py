Text_List=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'

def TextRead(file):
     #将txt文件转化为字符串
    with open(file,"r") as f :
        TextContent = f.read()
    return TextContent 

Text=TextRead('vigenere.txt')
Text=list(Text)
Str='' 
i=29
for y in range(i,len(Text),29):
    Str+=Text[y]
print(Str)


