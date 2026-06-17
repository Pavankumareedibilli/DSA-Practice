def FindMissingNumber(nums:list)->int:
    n = len(nums)
    m=n+1
    curr_sum=0
    for num in nums:
        curr_sum = curr_sum +num
    actual_sum = (m*(m+1))//2
    
    return actual_sum-curr_sum

arr = [8, 2, 4, 5, 3, 7, 1]
print(FindMissingNumber(arr))
