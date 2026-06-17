def left_rotate_by_one(nums:list):
    n = len(nums)
    if n==0 or n==1:
        return nums
    temp = nums[0]
    for i in range(n-1):
        nums[i]=nums[i+1]
    nums[-1]=temp

    return nums

print(left_rotate_by_one([1,2,3,4,5]))