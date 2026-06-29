def longestCommonPrefix(list:list)->str:
    if not list:
        return ""
    
    prefix = list[0]

    for s in list[1:]:
        i=0
        while i<len(prefix) and i<len(s) and prefix[i]==s[i]:
            i = i+1
        prefix = prefix[:i]
    
    if not prefix:
        return ""
    
    return prefix


def longestCommonPrefixOptimal(list:list)->str:
    n = len(list)
    list.sort()
    first = list[0]
    last = list[n-1]
    res = []

    for i in range(min(len(first),len(last))):
        if first[i]==last[i]:
            res.append(first[i])
        else:
            break

    return "".join(res)
            


list = ["pavan","pavan","pavban"]

print(longestCommonPrefixOptimal(list))
    