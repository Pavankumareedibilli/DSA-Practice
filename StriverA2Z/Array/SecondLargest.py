def SecondLargest(nums:list):
    Largest = nums[0]
    Second = nums[0]
    for num in nums:
        if num>Largest:
            Second =  Largest
            Largest = num
        if Largest>num>Second:
            Second = num
    print(Second)


SecondLargest([1,2,3,4,3,2,])