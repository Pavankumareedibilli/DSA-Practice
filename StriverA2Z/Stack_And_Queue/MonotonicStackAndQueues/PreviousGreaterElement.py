def previous_greater(nums:list)->list:
    n = len(nums)
    stack = []
    ans = [-1]*n

    for i in range(n):
        while stack and nums[stack[-1]]<=nums[i]:
            stack.pop()
        if stack:
            ans[i] = nums[stack[-1]]
        stack.append(i)
    return ans

nums = [2,3,1,2]
print(previous_greater(nums))

