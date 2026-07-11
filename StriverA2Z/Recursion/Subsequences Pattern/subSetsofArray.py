def subSetsofArray(nums):
    result = []
    def fun(idx,arr):

        if idx==len(nums):
            result.append(arr[:])
            return
        arr.append(nums[idx])
        fun(idx+1,arr)
        arr.pop()
        fun(idx+1,arr)

    fun(0,[])
    return result

arr = [1,2,3]

print(subSetsofArray(arr))


def subSetsofArraySum(nums):
    result = []
    def fun(idx,arr,sum):
        
        if idx==len(nums):
            result.append(sum)
            return
        
        arr.append(nums[idx])
        sum = sum + nums[idx]

        fun(idx+1,arr,sum)

        sum = sum - arr.pop()
        
        fun(idx+1,arr,sum)

    fun(0,[],0)
    return result

arr = [1,2,3]

print(subSetsofArray(arr))