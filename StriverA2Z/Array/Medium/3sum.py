def threeSum(nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1

            while left<right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left = left + 1
                elif total > 0:
                    right = right - 1
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    left = left + 1
                    right = right -1

                    while left < right and nums[left] == nums[left-1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right+1]:
                        right = right - 1
        return ans

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))