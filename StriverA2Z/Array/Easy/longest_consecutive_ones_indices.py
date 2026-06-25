def longest_consecutive_ones_indices(nums:list):
    CurrentCount = 0
    MaxCount = 0

    currentStart = -1
    bestStart=-1
    bestEnd = -1

    for i in range(len(nums)):
        if nums[i] ==1:
            if i ==0 or nums[i-1]==0:
                currentStart = i
            CurrentCount +=1
            if CurrentCount>MaxCount:
                MaxCount=CurrentCount
                bestStart = currentStart
                bestEnd = i
        else:
            CurrentCount = 0
    return bestStart,bestEnd


arr = [0, 1, 1, 1, 0, 1, 1]
print(longest_consecutive_ones_indices(arr))