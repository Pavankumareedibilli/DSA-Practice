def previous_smaller(arr):
    stack = []
    ans = []

    for x in arr:
        while stack and stack[-1] >= x:
            stack.pop()

        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])

        stack.append(x)

    return ans


print(previous_smaller([4, 5,1, 2, 3,10, 8]))