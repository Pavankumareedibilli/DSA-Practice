def nextgreaterelement(nums):
    result = [-1] *len(nums)
    stack =[]

    for i in range(len(nums)):
        while result and nums[i] > nums[stack[-1]]: 
            result[stack.pop()] = nums[i]
        stack.append(i)

    return result