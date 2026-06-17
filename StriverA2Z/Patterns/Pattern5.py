def Pattern(N):
    temp = N
    for i in range(N):
        for j in range(temp):
            print("*",end=" ")
        print()
        temp = temp - 1


Pattern(5)


# * * * * * 
# * * * * 
# * * * 
# * * 
# * 