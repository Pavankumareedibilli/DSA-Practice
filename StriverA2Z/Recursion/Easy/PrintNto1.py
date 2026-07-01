def fun(N):
    if N == 0:
        return
    print(N)
    fun(N-1)

fun(5)