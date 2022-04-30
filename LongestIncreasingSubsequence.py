import random as r

def lis(seq):
   L = [1 for _ in range(len(seq))]

   for i in range(1, len(L)):
      subproblems = [L[k] for k in range(i) if seq[k] < seq[i]]
      print(f"{i}, {subproblems}")
      L[i] = 1 + max(subproblems, default=0)
   return max(L, default=0)

A = [r.randrange(-5,10) for _ in range(20)]
print(A)
print(lis(A))
