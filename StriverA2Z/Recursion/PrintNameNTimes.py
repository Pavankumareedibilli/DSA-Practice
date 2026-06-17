def fun(N:int,name:str):
    if N==0:
        return
    print(name)
    fun(N-1,name)

fun(5,"pavan")