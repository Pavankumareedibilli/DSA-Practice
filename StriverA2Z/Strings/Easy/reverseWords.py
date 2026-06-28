def reverseWords(s:str)->str:
    words = s.split()
    words.reverse()
    return " ".join(words)


def reverseWordsOptimal(s:str)->str:
    i = 0
    n = len(s)
    stack=[]

    while i<n:
        while i<n and s[i] == " ":
            i = i+1

        word = []

        while i<n and s[i]!=" ":
            word.append(s[i])
            i = i+1
            
        if word:
            stack.append("".join(word))
    
    ans = []
    while stack:
        ans.append(stack.pop())
    
    return " ".join(ans)


s = "  Pavan   Kumar"

print(reverseWords(s))
print(reverseWordsOptimal(s))
