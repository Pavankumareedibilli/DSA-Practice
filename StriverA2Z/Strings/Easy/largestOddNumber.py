def largestOddNumber(s:str)->str:
    n = len(s)
    start = 0
    while start < n and s[start] == "0":
        start = start + 1
    
    end = n-1

    while end >= 0 and int(s[end])%2==0:
        end = end -1

    if end == -1 or start > end:
        return ""
    
    return s[start:end+1]


s = "00001234"
print(largestOddNumber(s))