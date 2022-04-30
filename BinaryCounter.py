class Digit:
   def __init__(self, length):
      self.value = 0
      self.length = length
      if self.length > 1:
         self.next = Digit(self.length - 1)
      else:
         self.next = None

   def __repr__(self):
      if self.next == None:
         return str(self.value)
      else:
         return self.next.__repr__() + str(self.value)

   def reset(self):
      self.value = 0
      if not self.next == None:
         self.next.reset()

   def inv_reset(self):
      self.value = 1
      if not self.next == None:
         self.next.inv_reset()

   def plus1(self):
      if self.value:
         if self.next == None:
            self.reset()
            return
         else:
            self.next.plus1()
      self.value = int(not self.value)

   def add(self,intnum):
      for _ in range(intnum):
         self.plus1()

   def minus1(self):
      if not self.value:
         if self.next == None:
            self.inv_reset()
            return
         else:
            self.next.minus1()
      self.value = int(not self.value)

   def subt(self,intnum):
      for _ in range(intnum):
         self.minus1()

a = Digit(8)
print(a)

print(a)

print(a)

print(a)

input()

   
         
