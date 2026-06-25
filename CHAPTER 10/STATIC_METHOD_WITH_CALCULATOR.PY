import math

class calculator:
    def __init__(self,number):
        self.square = number*number
        self.cube = number*number*number
        self.squareroot = math.sqrt(number)

    @staticmethod
    def greet():
        print("Good morning")

number = int(input("Enter a number: "))
cal = calculator(number)
cal.greet()
print(cal.square)
print(cal.cube)
print(cal.squareroot)