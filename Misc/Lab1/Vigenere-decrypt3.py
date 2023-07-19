text ='>;  +00  +;0qn^5 EEiT6Td!!ds!;h!EETT1T  }!O16 } QSETEd s1 ^0T}T+^ 11 O;&0&;!1d+ Td ;E;^ \nm;s^E T+1+ndh15&0T^0;}^ T^T^OO0;}  !& ;;;TT0m^'
frequency = {key:0 for key in text}  #初始化一个空字典

# 遍历文本中的每个字符
for x in text:
    if x in frequency:
        frequency[x] += 1  
    else:
        frequency[x] = 1  
for i in frequency:
    frequency[i]/=len(text)

# 输出字符频率
sorted_frequency=dict(sorted(frequency.items(),key = lambda x:x[1],reverse=True))
for char, count in sorted_frequency.items():
    print(f"Character '{char}' appears {count} ")



   