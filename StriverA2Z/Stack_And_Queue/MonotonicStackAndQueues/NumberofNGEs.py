def NGE(nums:list)->list:
    n = len(nums)
    result = [-1] *n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
            
        stack.append(i)
    return result

arr = [1, 3, 2, 4]  
print(NGE(arr))

arr = [6, 8, 0, 1, 3]  
print(NGE(arr))
