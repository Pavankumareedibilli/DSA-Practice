def calPrefix(arr):
    prefix = [0]*len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1]+arr[i]

    return prefix

def rangeSumQuery(arr,quries):
    prefix = calPrefix(arr)
    result = []
    for  l,r in quries:
        result.append(prefix[r]-prefix[l-1])
    
    return result
