import random as r

with open('subs.txt', "r", encoding='utf8') as f:
   subs = f.read()

subs = subs.split("\n")

print(r.choice(subs))
input()
