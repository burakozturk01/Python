from PIL import Image
import numpy as np
import math

def issq(x):
   root = math.sqrt(x)
   return int(root + 0.5) ** 2 == x

binary = input("Binary: ")
binlen = len(binary)

print(f"Length = {binlen}")

wr = math.ceil(math.sqrt(binlen))
while binlen % wr != 0:
   wr += 1
hr = int(binlen / wr)

print("Width * Height can't be smaller than binary length")
print(f"Recommendation: {wr} x {hr} (y/n)")

useRec = input() == "y" or input == "Y"
if useRec:
   w = wr
   h = hr
else:
   w = int(input("Width: "))
   h = int(input("Height: "))

   while w*h < len(binary):
      w = int(input("Width: "))
      h = int(input("Height: "))

print(f"Output size will be {w} x {h}")

while w*h > len(binary):
   binary += "0"

print("Binary stream filled to the desired size")

factor = int(input("Pixel size multiplier (1 for from one bit to one pixel conversion)"))

pixels = []

print("Generating pixels...")

for y in range(h):
   row = []
   for x in range(w):
      if binary[w*y+x] == "0":
         for _ in range(factor):
            row.append((0,0,0))
      elif binary[w*y+x] == "1":
         for _ in range(factor):
            row.append((255,255,255))
      else:
         for _ in range(factor):
            row.append((255,0,0))
   for _ in range(factor):
      pixels.append(row)

print("Pixel generation is done\nArray will be generated")

arr = np.array(pixels, dtype=np.uint8)

print("Array is generated\nImage will be generated")

img = Image.fromarray(arr)

print("Image is generated.\nPlease input file name")
filename = input()

img.save(f"{filename}.png")
print(f"Image saved as {filename}.png")
input()
