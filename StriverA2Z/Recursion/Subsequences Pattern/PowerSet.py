def generate_subsequences(s:str)->list:
    result = []

    def backtrack(curr:str,i:int):
        if i==len(s):
            result.append(curr)
            return

        backtrack(curr+s[i],i+1)
        backtrack(curr,i+1)
    
    backtrack("",0)

    return result

s="abc"
print(generate_subsequences(s))