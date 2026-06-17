def isSorted(nums:list):
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            return False
        
    return True

print(isSorted([1,2,2,4,6,7,9]))