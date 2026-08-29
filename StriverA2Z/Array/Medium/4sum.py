def fourSum(nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n-3):
            if i>0 and nums[i] == nums [i-1]:
                continue
                
            for j in range(i+1,n-2):
                
                if j> i+1 and nums[j] == nums[j-1]:
                    continue

                left = j+1
                right = n-1
                
                while left<right:
                    sum = nums[i]+nums[j]+nums[left]+nums[right]

                    if sum > target:
                        right = right - 1
                    elif sum< target:
                        left = left + 1
                    else:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left = left +1
                        right = right -1

                        while left < right and nums[left] == nums[left - 1]:
                            left = left + 1
                        while left < right and nums[right] == nums[right+1]:
                            right = right - 1
                    
        return result


nums = [1,0,-1,0,-2,2]
target = 0

print(fourSum(nums,target))