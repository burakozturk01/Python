import copy
import random

class BigNum:

   def __init__(self, nList):
      if nList != []:
         self.digits = nList
      else:
         digits = []
         self.digits = digits
                        
   def toString(self):
      st = ""
      
      for i in range(len(self.digits)):
         st += str(int(self.digits[i]))
         if (i + 1) % 3 == 0:
            st += "."

      return st[::-1]

   def addDigit(self, digit):
      if digit >= 0 & digit < 10:
         self.digits.append(digit)
      else:
         print("olmaz")

   def add(self, num):
      sNum1 = copy.deepcopy(self.digits)
      sNum2 = copy.deepcopy(num.digits)
      sumNum = []
      dsum = 0
      carry = 0
      temp = 0

      if len(sNum1) > len(sNum2):
         while len(sNum1) > len(sNum2):
            sNum2.append(0)
         print("self>num")
      elif len(sNum1) < len(sNum2):
         while len(sNum1) < len(sNum2):
            sNum1.append(0)
         print("self<num")
      for i in range(len(sNum1)):
         temp = int(sNum1[i] + sNum2[i] + carry)
         dsum = int(temp % 10)
         carry = int((temp - dsum) / 10)
         sumNum.append(dsum)
      self.digits = sumNum
      return
      
                
list1 = []
list2 = []

for i in range(100000):
   list1.append(int( random.randint(0, 9)))
for i in range(100000):
   list2.append(int( random.randint(0, 9)))

n1 = BigNum(list1)
n2 = BigNum(list2)

print(n1.toString())

print(n2.toString())

n1.add(n2)
print(n1.toString())
input()
