def MajorityElement(nums:list)->int:
    HashMap = {}
    for i in range(len(nums)):
        HashMap[nums[i]] = HashMap.get(nums[i],0)+1
    
    for key,val in HashMap.items():
        if val > len(nums)//2:
            return key
    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
print(MajorityElement(arr))