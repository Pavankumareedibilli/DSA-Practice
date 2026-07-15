def letterCombinations(digits:str)->list:
    if not digits:
        return []
    
    result = []

    mapping = {
        "2":"abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def dfs(index,current):

        if index == len(digits):
            result.append(current)
            return
        
        for ch in mapping[digits[index]]:
            dfs(index+1,current+ch)

    dfs(0,"")
    return result

digits = "23"
print(letterCombinations(digits))
