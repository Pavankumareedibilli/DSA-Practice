def next_greater_idx(nums:list)->list:
    n = len(nums)
    stack = []
    ans = [-1]*n

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            ans[idx] = i
        stack.append(i)
    return ans
