def nextSmallestElement(nums):
    stack = []
    answer = [-1] * len(nums)

    for i in range(len(nums)):

        while stack and nums[i]<nums[stack[-1]]:
            answer[stack.pop()] = nums[i]
        stack.append(i)
    return answer

print(nextSmallestElement([3,4,1,6,5,2]))