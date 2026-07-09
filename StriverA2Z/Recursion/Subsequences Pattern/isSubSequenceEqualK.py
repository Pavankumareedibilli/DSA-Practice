def isSubSequenceEqualK(nums:list,k:int) -> bool:
    n = len(nums)
    def bfs(idx,sum):
        if sum < 0 or idx == n:
            return False
        if sum == 0:
            return True
        return bfs(idx+1,sum-nums[idx]) or bfs(idx+1,sum)
    return bfs(0,k)

nums = [4, 3, 9, 2] 
k = 10
print(isSubSequenceEqualK(nums,k))

nums = [1, 2, 3, 4, 5]
k = 8
print(isSubSequenceEqualK(nums,k))  