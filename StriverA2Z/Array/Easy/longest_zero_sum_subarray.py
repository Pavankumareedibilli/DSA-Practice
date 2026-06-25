def longest_zero_sum_subarray(nums:list)->int:
    HashMap ={}
    prefixsum = 0
    maxLength = 0
    for i,val in enumerate(nums):
        prefixsum = prefixsum + val
        if prefixsum in HashMap:
            length = i - HashMap[prefixsum]
            maxLength = max(maxLength,length)
        else:
            HashMap[prefixsum] = i 
    return maxLength


arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(longest_zero_sum_subarray(arr))