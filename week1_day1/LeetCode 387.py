def fisrtUniqChar(s):
    char_dict={}
    for i in s:
        char_dict[i]=char_dict.get(i,0)+1
    for index,char in enumerate(s):
        if char_dict[char]==1:
            return [char,index]
    return -1

print(fisrtUniqChar('leetcodel'))
