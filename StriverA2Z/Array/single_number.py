def single_number(nums:list)->int:
    Result = 0
    for num in nums:
        Result = Result ^ num
    return Result


def single_number_hashmap(nums:list)->int:
    HashMap = {}
    for num in nums:
        HashMap[num]=HashMap.get(num,0)+1
    for key,value in HashMap.items():
        if value % 2 == 1:
            return key
    return -1



nums = [2,1,3,2,1]

print(single_number_hashmap(nums))