def decToHex(dec, prefix = False):
   # Eliminate zero cases
   if dec == 0:
      return "0"

   # Result string
   hexed = ""

   # Handle negatives
   if dec < 0:
      hexed += "-"
      dec *= -1

   # Optional 0x prefix
   if prefix:
      hexed += "0x"

   # Digit number starting from least significant digit
   digit = 0

   # Finding MSD's index
   while 16**digit <= dec:
      digit += 1
   digit -= 1

   # List for hexadecimal only digits
   digits = ['A','B','C','D','E','F']

   # Main loop
   # Handling every digit from MSD to LSD
   while digit > -1:
      count = 0
      
      # Counting digits from input
      while 16**digit <= dec:
         dec -= 16**digit
         count += 1
         
      # Adding digits to result
      if 0 <= count < 10:
         hexed += str(count)
      else:
         hexed += digits[count - 10]

      # Next digit
      digit -= 1
      
   return hexed

def hexToDec(hexStr):
   # Empty str case
   if hexStr == "":
      return None

   # Return variable and negative coverage
   dec = 0
   neg = False

   # Detect negatives
   if hexStr[0:1] == "-":
      hexStr = hexStr[1:]
      neg = True

   # Detect 0x prefixes
   if hexStr[0:2] == "0x":
      hexStr = hexStr[2:]

   # Uppercase and reverse the string
   hexStr = hexStr.upper()
   hexStr = hexStr[::-1]

   # Digit number starting from most significant digit
   digCount = 0

   # List for hexadecimal only digits
   hexDigs = ['A','B','C','D','E','F']

   # Main loop
   # Handling every digit from LSD to MSD
   while len(hexStr) > 0:
      # Handling dec digits 0-9
      if hexStr[0:1].isdigit():
         dec += (16**digCount) * int(hexStr[0:1])
         
      # Handling hex digits A-F
      elif hexStr[0:1] in hexDigs:
         dec += (16**digCount) * (int(hexDigs.index(hexStr[0:1]))+10)
         
      # Everything else is illegal
      else:
         return "Invalid input"

      # Next digit
      digCount += 1
      hexStr = hexStr[1:]

   # Negatives
   if neg:
      dec *= -1

   return dec

# Input can only contain '0's and '1's
# Any prefix other than negative sign '-' is invalid
# Input must be unsigned binary string, does not support 1's nor 2's compliment
def binToHex(binStr):
   if binStr == "":
      return ""
   
   neg = False
   if binStr[0] == '-':
      binStr = binStr[1:]
      neg = True
      
   if (binStr.count('0') + binStr.count('1')) != len(binStr):
      return "Invalid input"
   
   while not len(binStr) % 4 == 0:
      binStr = '0' + binStr

   binBlocks = []
   while len(binStr) > 0:
      binBlocks.append(binStr[0:4])
      binStr = binStr[4:]

   hexDigs = ['0', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' ]
   
   binList = ['0000', '0001', '0010', '0011',
              '0100', '0101', '0110', '0111',
              '1000', '1001', '1010', '1011',
              '1100', '1101', '1110', '1111']

   hexStr = ""
   for binBlock in binBlocks:
      hexStr += hexDigs[binList.index(binBlock)]

   if neg:
      hexStr = '-' + hexStr

   return hexStr

def hexToBin(hexStr):
   if hexStr == "":
      return ""

   # Detect negatives
   neg = False
   if hexStr[0:1] == "-":
      hexStr = hexStr[1:]
      neg = True

   if len(hexStr) == hexStr.count('0'):
      return '0'

   # Detect 0x prefixes
   if hexStr[0:2] == "0x":
      hexStr = hexStr[2:]

   hexStr = hexStr.upper()

   digs = []
   while len(hexStr) > 0:
      digs.append(hexStr[0:1])
      hexStr = hexStr[1:]

   hexDigs = ['0', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' ]
   
   binList = ['0000', '0001', '0010', '0011',
              '0100', '0101', '0110', '0111',
              '1000', '1001', '1010', '1011',
              '1100', '1101', '1110', '1111']

   binStr = ""
   for dig in digs:
      if not dig in hexDigs:
         return "Invalid input"
      binStr += binList[hexDigs.index(dig)]

   while binStr[0] == '0':
      binStr = binStr[1:]
   
   if neg:
      binStr = '-' + binStr

   return binStr

inp1 = ""
inp2 = ""
while 1:
   print("Select conversion types: ")
   print("   1: Decimal to hexadecimal")
   print("   2: Hexadecimal to decimal")
   print("   3: Binary to hexadecimal\n      (Compliments and prefixed other than '-' are not supported)")
   print("   4: Hexadecimal to binary")
   print("Exit: Close the program\n\nSelect: ", end="")

   inp1 = input()

   if inp1 == '1':
      inp2 = input("Enter decimal value: ")
      print("Hexadecimal equivalent:", decToHex(int(inp2)), end="\n\n")
      continue
   elif inp1 == '2':
      inp2 = input("Enter hexadecimal value: ")
      print("Decimal equivalent:", hexToDec(inp2), end="\n\n")
      continue
   elif inp1 == '3':
      inp2 = input("Enter binary value: ")
      print("Hexadecimal equivalent:", binToHex(inp2), end="\n\n")
      continue
   elif inp1 == '4':
      inp2 = input("Enter hexadecimal value: ")
      print("Binary equivalent:", hexToBin(inp2), end="\n\n")
      continue
   if inp1.lower() == "exit":
      print("Goodbye")
      input()
      break
   print("Invalid input\n\n")
