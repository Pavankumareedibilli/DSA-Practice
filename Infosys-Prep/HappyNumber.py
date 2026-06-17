def HappyNumber(num):
    visited = set()

    while num not in visited:
        visited.add(num)
        num = findsumofsqures(num)
        if num == 1:
            return True
    return False   
    

def findsumofsqures(num):
    ans = 0
    while num:
        digit = num%10  
        ans = ans + digit **2
        num = num // 10
    return ans

print(HappyNumber(19))