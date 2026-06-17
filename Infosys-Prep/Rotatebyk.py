def Rotate(nums:list,k:int):
    n = len(nums)
    k = k%n
    result = [0]*n
    for i in range(n):
        new_idx = (i+k)%n
        result[new_idx] = nums[i]
    return result

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

print(Rotate(nums,k))
