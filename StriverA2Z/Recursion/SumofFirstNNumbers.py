def fun(N) ->int:
    if N==1:
        return 1
    return N+fun(N-1)
print(fun(3))