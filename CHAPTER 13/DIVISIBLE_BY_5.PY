def divisible(n):
    if(n%5 == 0):
        return True
    return False

a = [1,236464,356465,3464640]

f = list(filter(divisible, a))
print(f)