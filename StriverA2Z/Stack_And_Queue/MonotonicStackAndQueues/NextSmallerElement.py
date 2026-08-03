def next_smaller(nums:list)->list:
    n = len(nums)
    stack = []
    ans = [-1]*n

    for i in range(n):
        while stack and nums[i]<nums[stack[-1]]:
            idx = stack.pop()
            ans[idx] = nums[i]
        stack.append(i)

    return ans

nums = [2,3,4,2]

print(next_smaller(nums))