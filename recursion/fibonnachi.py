import timeit

def fibo(n):
    if n == 1:
        return 1
    if n == 0 :
        return 0
    return fibo(n-2) + fibo(n-1)

timeit.timeit(fibo(9))

