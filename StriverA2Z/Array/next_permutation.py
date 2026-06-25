def next_permutation(nums:list)->list:
    n = len(nums)
    pivot = -1

    for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            pivot = i
            break

    if pivot == -1:
        return nums.reverse()
     
    
    for i in range(n-1,pivot,-1):
        if nums[i]> nums[pivot]:
            nums[pivot],nums[i] = nums[i],nums[pivot]
            break
    
    left = pivot + 1
    right = n-1
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]
        left = left +1
        right = right-1
    return nums


nums = [1, 2, 7, 4, 3, 1]
print(next_permutation(nums))