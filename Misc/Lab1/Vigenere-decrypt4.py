Text_List=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'
for key in range(97):
    if (Text_List.index('e')*key)%97==Text_List.index('}'):
        print(Text_List[key])