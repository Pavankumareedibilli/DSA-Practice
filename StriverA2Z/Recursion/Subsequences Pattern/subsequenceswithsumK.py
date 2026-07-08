def subsequenceswithsumK(nums,k):
    result = 0
    def bfs(curr_sum,i):
        nonlocal result
        if i == len(nums):
            if curr_sum == k:
                result +=1
            return

        bfs(curr_sum+nums[i],i+1)
        bfs(curr_sum,i+1)
    
    bfs(0,0)
    
    return result


nums = [4, 9, 2, 5, 1]
print(subsequenceswithsumK(nums,10))

nums = [4, 2, 10, 5, 1, 3]
print(subsequenceswithsumK(nums,5))