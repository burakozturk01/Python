from decimal import *

getcontext().prec = int(input("Precision: "))

a = Decimal("1")
b = Decimal("1")
ratio = 0

while 1:
   t = a + b
   a = b
   b = t

   if ratio == b/a:
      break
   else:
      ratio = b/a

print(f"e approximated as {ratio}")
input()
