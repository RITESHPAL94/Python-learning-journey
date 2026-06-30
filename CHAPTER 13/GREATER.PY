from functools import reduce
l = [1, 23, 6464, 356, 465, 3464, 640]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))