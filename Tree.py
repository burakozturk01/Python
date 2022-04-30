class Tree:
   count = 0

   def __init__(self, value):
      self.branches = [None,None,None]
      self.value = value

   def left(self):
      return self.branches[0]
   def middle(self):
      return self.branches[1]
   def right(self):
      return self.branches[2]

   def set_left(self, value):
      self.left() = Tree(value)
   def set_middle(self, value):
      self.middle() = Tree(value)
   def set_right(self, value):
      self.right() = Tree(value)

