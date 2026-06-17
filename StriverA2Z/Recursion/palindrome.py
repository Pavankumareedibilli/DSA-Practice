def fun(i,s):
    if i>=len(s)//2:
        return True
    if s[i] !=  s[len(s)-i-1]:
        return False
    return fun(i+1,s)

print(fun(0,"pavnavap"))
