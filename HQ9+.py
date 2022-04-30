# HQ9+ is an esoteric programming language and this is a python implementation

# HQ9+ reads its code char by char and performs according to chars
# H: Prints hello world. Therefore HQ9+'s hello world program has single byte source code.
# Q: Prints program's source code. Therefore HQ9+'s quine is also 1 byte long.
# 9: Prints 99 bottles of beer. Over explaining became boring and u got it.
# +: Okay this is a good one. HQ9+ has a memory of one integer named accumulator, it starts as 0 and '+' adds 1 to it.
#    and that's it. You can't use accumulator's in any way. Best Lang Ever.

while 1:
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
            print(f"Take one down, pass it around,\n{i-1} bottles of beer on the wall.", end="")
         print("1 bottle of beer on the wall,\n1 bottle of beer.\nTake one down, pass it around,\nno more bottles of beer on the wall.")
      elif c == '+':
         accumulator += 1
