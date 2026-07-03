def generateParenthesis(n:int)->list:
    Result = []
    def generate(curr,openCount,closeCount):
        if len(curr) == 2*n:
            Result.append(curr)
            return

        if openCount<n:
            generate(curr + "(", openCount+1, closeCount)
        
        if openCount>closeCount:
            generate(curr +")", openCount, closeCount+1)
        
    generate("",0,0)

    return Result

n = 3
print(generateParenthesis(n))
