def LargestElement(nums:list):
    Largest = nums[0]
    for num in nums:
        if num>Largest:
            Largest = num
    print(Largest)


LargestElement([1,2,3,2,1,4,2])