import math as m

def function1 (x,y):
    return -(x/y) *(m.log(x/y))

function1(10,2)

def function2 (x):
    return 1/(1+m.exp(-x))

function2(1)

def function3 (x,x2):
    return (m.exp(x))/(m.exp(x**2))

function3(5 , 8)

def function4 (x,y,y2):
    return (1/x) *(y-y2)

function4(1,4,3)

def function5 (x):
    return m.sqrt (x * m.log(x))

function5(5)