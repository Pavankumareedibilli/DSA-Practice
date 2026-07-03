def DepthofParenthesis(s:str)->int:
    maxLength = 0
    stack = []
    currLength = 0
    for char in s:
        if char == "(":
            currLength = currLength + 1
            stack.append(char)
            maxLength = max(maxLength,currLength)
        elif char == ")":
            if stack:
                stack.pop()
                currLength = currLength - 1 
            else:
                return 0
    if stack:
        return 0
    
    return maxLength

s = "(1+(2*3)+((8)/4))+1"
s2 = "(1)+((2))+(((3)))"
print(DepthofParenthesis(s2))