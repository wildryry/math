import numpy as np

# F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)



def myfib(n):
    if n == 0 or n == 1:
        
        return n
    else:
        
        return myfib(n-1) + myfib(n-2)

def debug_fib(fibalg, n):
    counter = 0
    return fibalg(n,counter), counter

