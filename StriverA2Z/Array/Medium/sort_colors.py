def sort_colors(nums:list)->list:
    n = len(nums)
    count0 = 0
    count1 = 0
    for i in range(n):
        if nums[i] == 0:
            count0 +=1
        if nums[i] == 1:
            count1 += 1
    for i in range(n):
        if i < count0:
            nums[i]=0
        elif i < count0 + count1:
            nums[i]=1
        else:
            nums[i]=2
    return nums

def sort_colors_optimal(nums:list)->list:
    low = 0
    mid = 0
    high = len(nums)-1
    while mid < high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low = low +1
            mid = mid +1
        elif nums[mid] == 1:
            mid = mid +1
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high = high -1



nums = [2, 0, 2, 1, 1, 0]

sort_colors_optimal(nums)

print(nums)
# [0, 0, 1, 1, 2, 2]

