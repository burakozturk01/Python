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

def binToDec(binStr):
   return hexToDec(binToHex(binStr))

def binDecoder(binStr, wanted = None):
	for pLen in range(1, len(binStr)+1):
		for disp in range(len(binStr) - pLen + 1):
			substr = binStr[disp:disp+pLen]
			subdec = binToDec(substr)
			if wanted == None:
				print(subdec)
			elif subdec == wanted:
				print(f"Index of {substr} starts at {disp}")
				return

if __name__ == "__main__":
   binDecoder(input())
