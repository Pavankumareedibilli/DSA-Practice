def countfreq(nums:list):
    dict = {}
    for num in nums:
        dict[num] = dict.get(num,0)+1
    for key,value in dict.items():
        print(key,value)

countfreq([1,1,3,4,2,4])


