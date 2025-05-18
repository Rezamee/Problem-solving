def rev (x):
    if len(x) ==0:
        return x
    else :
        return rev (x[1:])+x[0]
rev ("amin")