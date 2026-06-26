class Number:
   def __init__(self, n):
      self.n = n

   def __add__(self, Num):
      return self.n + Num.n

n = Number(1)
m = Number(2)

print(n + m)