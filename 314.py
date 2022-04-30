from decimal import *

getcontext().prec = int(input("Precision: "))

sum = Decimal("0")
i = Decimal("1")
exsum = Decimal("31")
zeros = "0"

while 1:
   sum += 1/i**2
   i += 1

   if str(i)[1:] == zeros:
      zeros += "0"
      print(f"{i} terms calculated.\n...")

   if exsum == sum:
      break
   else:
      exsum = sum

sum = sum * 6
sum = sum.sqrt()
print(f"Pi approximated as {sum} by adding {i} terms.")
input()
