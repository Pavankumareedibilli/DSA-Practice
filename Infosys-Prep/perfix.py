def build_prefix_sum(arr):
    prefix=[0]*len(arr)
    prefix[0]=arr[0]

    for i in range(1,len(arr)):
        prefix[i] = arr[i] + prefix[i-1]
    
    return prefix

def range_sum_quries(arr , queries):
    prefix = build_prefix_sum(arr)
    result =[]
    for l,r in queries:
        if l == 0:
            result.append(prefix[r])
        else:
            result.append(prefix[r]-prefix[l-1])

    return result