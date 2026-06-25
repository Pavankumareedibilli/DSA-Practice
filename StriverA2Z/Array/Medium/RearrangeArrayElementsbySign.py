def RearrangeArrayElementsbySign(nums:list)->list:
    result = len(nums)*[0]
    posIdx = 0
    negIdx = 1
    for num in nums:
        if num > 0:
            result[posIdx]=num
            posIdx = posIdx +2
        else:
            result[negIdx]=num
            negIdx = negIdx+2
    return result

nums = [2,3,-1,-14,4,-9]
print(RearrangeArrayElementsbySign(nums)) 