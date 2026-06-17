from math import gcd

def GCD(nums:list):
    g = nums[0]
    for i in range(1,len(nums)):
        g = gcd(g,nums[i])
    return g

arr = [12,18,24]
print(GCD(arr))
