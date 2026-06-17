def fun(N):
    if N == 0:
        return
    fun(N-1)
    print(N) 
    
    
fun(5)

