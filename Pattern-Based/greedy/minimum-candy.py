def candy(ratings:list)->int:
    n = len(ratings)
    left = [1] * n
    right = [1] * n

    result = 0

    for i in range(1,n):
        if ratings[i]>ratings[i-1]:
            left[i]= left[i-1] + 1

    for i in range(n-1):
        if ratings[i]>ratings[i+1]:
            right[i] = right[i+1] + 1

    for i in range(n):
        result = result + max(left[i],right[i])

    return result


ratings = [1,2,2]
print(candy(ratings))

    
