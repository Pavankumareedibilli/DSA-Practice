def left_rotate_k(nums:list,k:int):
    n = len(nums)

    if n<=1:
        return n
    
    k = k%n
    reverese(nums,0,k-1)
    reverese(nums,k,n-1)
    reverese(nums,0,n-1)


def reverese(nums,start,end):
    while start<=end:
        nums[start],nums[end] = nums[end],nums[start]
        start = start+1
        end = end-1


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

left_rotate_k(arr, k)

print(arr)