def Ladders(nums:list):
    if not nums:
        return []
    result = [nums[-1]]
    right_max = nums[-1]
    for i in range(len(nums)-2,-1,-1):

        if nums[i]>right_max:
            result.append(nums[i])
            right_max = nums[i]

    return result[::-1]


arr = [10, 22, 12, 3, 0, 6]
arr2 = [2,3,1] 
print(Ladders(arr2))