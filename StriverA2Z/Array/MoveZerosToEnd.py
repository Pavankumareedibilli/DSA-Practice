def MoveZerosToEnd(nums:list)->list:
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i]!=0:
            if i!=j:
                nums[j],nums[i]=nums[i],nums[j]
            j = j+1
    return nums

nums = [0, 1, 0, 3, 12]

MoveZerosToEnd(nums)

print(nums)