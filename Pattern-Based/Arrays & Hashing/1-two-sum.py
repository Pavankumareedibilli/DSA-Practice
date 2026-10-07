def twoSum(nums:list,target:int):
    seen ={}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement],i]

        seen[nums[i]] = i

    return []

def twoSumAllPairs(nums:list,target:int):
    freq = {}
    result = []

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in freq:
            for _ in range(freq[complement]):
                result.append((complement,nums[i]))

        freq[nums[i]] = freq.get(nums[i],0) + 1

    return result


def countPairs(nums:list,target):
    freq = {}
    count = 0

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in freq:
            count = count + freq[complement]

        freq[nums[i]] = freq.get(nums[i],0) + 1

    return count










nums = [1, 5, 7, -1, 5]
target = 6

print(twoSumAllPairs(nums, target))
print(twoSum(nums, target))
print(countPairs(nums, target))

