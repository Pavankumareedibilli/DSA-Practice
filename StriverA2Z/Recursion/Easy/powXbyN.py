def powXbyN(X:int,N:int):
    if N==0:
        return 1
    if N==1:
        return X
    return X*powXbyN(X,N-1)

print(powXbyN(2,10))