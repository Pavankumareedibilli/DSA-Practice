def MaximumConsecutiveOnes(nums:list)->int:
    CurrentCount=0
    MaxCount=0
    for num in nums:
        if num == 1:
            CurrentCount +=1
            MaxCount = max(MaxCount,CurrentCount)
        else:
            CurrentCount=0
    return MaxCount

nums =[1,0,1,1,1,0]

print(MaximumConsecutiveOnes(nums))
print(MaximumConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 3
print(MaximumConsecutiveOnes([0, 0, 0]))           # 0
print(MaximumConsecutiveOnes([1, 1, 1]))           # 3
print(MaximumConsecutiveOnes([]))                  # 0
