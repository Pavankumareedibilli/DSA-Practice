def two_sum(nums:list,K:int):
    if not nums:
        raise ValueError("No two values sum equal to K")
    HashMap = {}
    for i,val in enumerate(nums):
        if K-val in HashMap:
            idx = HashMap[K-val]
            return idx,i
        HashMap[val]=i
    return None

nums = [1,-2,3,4,5]

print(two_sum(nums,3))