import math

class calculator:
    def __init__(self,number):
        self.square = number*number
        self.cube = number*number*number
        self.squareroot = math.sqrt(number)

number = int(input("Enter a number: "))
cal = calculator(number)
print(cal.square)
print(cal.cube)
print(cal.squareroot)