def ImplementationofAtoi(s:str)->int:
    INT_MAX = 2**31 -1
    INT_MIN = -(2**31)
    i = 0 
    n = len(s)
    while i<n and s[i] == " ":
        i = i + 1
    
    sign = 1

    while i<n and s[i] in ["+","-"]:
        if s[i] == "-":
            sign = -1
        i = i + 1
        
    num = 0

    while i<n and s[i].isdigit():
        digit = int(s[i])
        num = num*10 + digit
        i = i + 1

    num = num * sign
    
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    
    return num

s = "4193 with words" 
print(ImplementationofAtoi(s))