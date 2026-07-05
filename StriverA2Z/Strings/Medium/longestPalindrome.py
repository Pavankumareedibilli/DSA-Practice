def longestPalindrome(s:str)->str:
    if len(s)<2:
        return s
    
    max_len = 1
    start = 0
    
    def expand(left,right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left = left -1
            right = right +1
        
        return left+1,right-1

    for i in range(len(s)):
        left,right = expand(i,i)

        if right-left+1 >max_len:
            start = left
            max_len = right-left+1

        
        left2,right2 = expand(i,i+1)

        if right2-left2+1 > max_len:
            start = left2
            max_len = right2-left2+1

    return s[start:start+max_len]
        

s = "ababakdb"

print(longestPalindrome(s))
        


    