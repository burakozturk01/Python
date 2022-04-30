accumulator = 0

sc = input()

for c in sc:
   if c == 'H' or c == 'h':
      print("Hello, World!")
   elif c == 'Q' or c == 'q':
      print(sc, end="")
   elif c == '9':
      for i in range(99, 0, -1):
         print(f"{i} bottles of beer on the wall,\n{i} bottles of beer.")
         print("Take one down, pass it around,\n{i-1} bottles of beer on the wall.", end="")
      print("1 bottle of beer on the wall,\n1 bottle of beer.\nTake one down, pass it around,\nno more bottles of beer on the wall.")
   elif c == '+':
      accumulator += 1
