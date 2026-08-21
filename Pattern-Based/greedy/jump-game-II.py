def minJumps(nums:list)->int:
    if len(nums)<=1:
        return 0 
    max_end = 0
    farthest = 0
    jumps = 0

    for i in range(len(nums)-1):
        farthest = max(farthest, i + nums[i])

        if i == max_end:
            max_end = farthest
            jumps = jumps + 1

    return jumps

nums = [8,3,0,1,2]
print(minJumps(nums))