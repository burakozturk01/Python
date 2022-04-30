import math as m

def approximateRecursive(smlrMediant, bgrMediant, ratioNum, maxError):
   if smlrMediant == 0 or bgrMediant == 1:
      return approximate([0, 1], [1, 1], ratioNum, maxError)
   
   newMediant = [ (smlrMediant[0] + bgrMediant[0]) , (smlrMediant[1] + bgrMediant[1]) ]

   if abs(newMediant[0] / newMediant[1] - ratioNum) < 10**(-1 * maxError):
      return f"{newMediant[0]} / {newMediant[1]}"

   elif smlrMediant[0] / smlrMediant[1] < ratioNum < newMediant[0] / newMediant[1]:
      return approximate(smlrMediant, newMediant, ratioNum, maxError)
   
   elif newMediant[0] / newMediant[1] < ratioNum < bgrMediant[0] / bgrMediant[1]:
      return approximate(newMediant, bgrMediant, ratioNum, maxError)

   else:
      return "Error"

def approximate(ratioNum, maxError):

   if not (0 < ratioNum < 1):
      ratioNum -= m.floor(ratioNum)
   
   smlr = [0,1]
   bgr = [1,1]

   mediant = [1,2]

   counter = 1

   while abs(mediant[0] / mediant[1] - ratioNum) > 10**(-1 * maxError):
      counter += 1
      
      if smlr[0] / smlr[1] < ratioNum < mediant[0] / mediant[1]:
         mediant = [smlr[0] + mediant[0], smlr[1] + mediant[1]]

         if ratioNum < mediant[0] / mediant[1]:
            bgr = mediant
         else:
            smlr = mediant

      elif mediant[0] / mediant[1] < ratioNum < bgr[0] / bgr[1]:
         mediant = [bgr[0] + mediant[0], bgr[1] + mediant[1]]

         if ratioNum < mediant[0] / mediant[1]:
            bgr = mediant
         else:
            smlr = mediant

   return f"Fraction: {mediant[0]}/{mediant[1]}\nDecimal repr: {mediant[0]/mediant[1]}\nError: {mediant[0]/mediant[1]-ratioNum}\nCounter: {counter}\n"
   
while 1:
   rational = input("Find approximation for: ")
   rational = float(rational)

   error = input("Max error can be 10^-?: ")
   error = int(error)

   print(approximate(rational, error))
