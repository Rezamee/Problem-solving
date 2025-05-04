import math as m

def func1 (z):
    if z>0 and z<=1:
       return z
    else:
       return 1/(1+m.exp(-z))
print(func1(2))

def func2 (x):
    if x<0:
        return x*-1
    else:
        return x
print(func2(-5))
print(func2(1))
print(func2(0))

