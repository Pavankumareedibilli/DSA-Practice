def subSet2(nums):
    result = []
    nums.sort()
    def fun(idx,curr):
        if idx == len(nums):
            result.append(curr[:])
            return

        curr.append(nums[idx])
        fun(idx+1,curr)
        curr.pop()

        while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
            idx = idx + 1

        fun(idx+1,curr)

    fun(0,[])
    return result

nums = [1,2,2,2]
print(subSet2(nums))
        