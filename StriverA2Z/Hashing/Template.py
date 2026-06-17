def Hasing(nums:list):
    dict = {}

    for num in nums:
        dict[num] = dict.get(num,0)+1
    return dict

print(Hasing([1,2,3,3,32,2,3,4,1]))