#!/usr/bin/python3
num1 = int(input('times what by 10? '))

def times_10(fnum1:int):
    fnum2 = fnum1 
    for x in range(10):
        fnum2 = (fnum1 + fnum2)
        print(x,fnum1,fnum2)
    fnum2 = (fnum2 - fnum1)
    return fnum2
	
num1 = times_10(num1)

print(num1)



