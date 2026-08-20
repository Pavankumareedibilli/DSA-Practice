def assign_cookies(g:list,s:list)-> int:
    g.sort()
    s.sort()
    child = 0
    cookie = 0
    while child<len(g) and cookie<len(s):
        if s[cookie]>=g[child]:
            child = child +1
            cookie = cookie +1
        else:
            cookie = cookie +1
    return child

g = [2,3,1]
s = [1,2]

print(assign_cookies(g,s))