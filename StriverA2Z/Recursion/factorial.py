def fun(N):
    if N==0:
        return 1
    return N*fun(N-1)

print(fun(5))