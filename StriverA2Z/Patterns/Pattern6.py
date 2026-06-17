def pattern(N):
    temp = N
    for i in range(N):
        for j in range(1,temp+1):
            print(j,end=" ")
        print()
        temp = temp - 1

pattern(5)


# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 