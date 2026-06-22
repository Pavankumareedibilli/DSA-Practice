def longest_subarray_with_sum_k(nums:list,k:int)->int:
    MaxLen = 0
    sum = 0
    left = 0
    for right in range(len(nums)):
        sum = sum + nums[right]
        while sum>k and left<=right:
            sum = sum - nums[left]
            left = left+1
        
        if sum == k:
            MaxLen = max(MaxLen,right-left+1)
    return MaxLen


nums = [1, 2, 1, 1, 1]
k = 3
print(longest_subarray_with_sum_k(nums, k))