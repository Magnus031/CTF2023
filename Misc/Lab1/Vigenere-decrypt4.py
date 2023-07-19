Text_List=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'
for key in range(97):
    if (Text_List.index('a')*key)%97==Text_List.index('Q'):
        print(Text_List[key])