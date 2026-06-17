def LinearSearch(nums:list,value)->int:
    for idx,val in enumerate(nums):
        if val == value:
            return idx
    return -1


nums=[2,3,1,4]
print(LinearSearch(nums,1))