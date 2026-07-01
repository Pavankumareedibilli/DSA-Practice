def IsomorphicString(s1:str,s2:str)->bool:
    if len(s1)!=len(s2):
        return False
    
    s1_to_s2={}
    s2_to_s1={}

    for i in range(len(s1)):
        ch1 = s1[i]
        ch2 = s2[i]

        if ch1 in s1_to_s2:
            if s1_to_s2[ch1] != ch2:
                return False
        else:
            s1_to_s2[ch1]=ch2
        
        if ch2 in s2_to_s1:
            if s2_to_s1[ch2] != ch1:
                return False
        else:
            s2_to_s1[ch2] = ch1

    return True

s1="paper"
s2 ="tikle"

print(IsomorphicString(s1,s2))
