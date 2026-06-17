def fun(N):
    if N<=1:
        return N
    return fun(N-1)+fun(N-2)


for i in range(5):
    print(fun(i))