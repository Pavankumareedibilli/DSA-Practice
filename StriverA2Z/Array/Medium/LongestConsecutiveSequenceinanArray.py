def longestConsecutive(nums:list[int]) -> int:
    result = 0
    seen = set(nums)
    length = 0
        
    for num in seen:
        if num-1 not in seen:
            length = 1
            current = num
            while current + 1 in seen:
                length = length + 1
                current = current + 1
            result = max(result,length)
    return result

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))

