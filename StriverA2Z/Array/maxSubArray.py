def maxSubArray(nums:list[int])->int:
    currentSum = nums[0]
    maxSum = nums[0]
    for num in nums:
        currentSum +=num
        currentSum = max(currentSum,num)
        maxSum = max(maxSum,currentSum)
    return maxSum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))