def MinAndMaxOccur(nums:list):
    dict = {}

    for num in nums:
        dict[num] = dict.get(num,0)+1
        
    min=len(nums)
    max=0
    maxans = 0
    minans=0
    for key,value in dict.items():
        if value > max:
            max = value
            maxans = key
        if value<=min:
            min = value
            minans = key
    print("Max occur elemnt ",maxans)
    print("min occur elemnt ",minans)

MinAndMaxOccur([1,1,1,1,2,3,3,3,4])
        
