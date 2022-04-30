import random

ints = []

for _ in range(100):
    ints.append(random.randint(-500,500))

f = open("try_file.txt", "w")
f.write("Random integers:\n")

for i in range(100):
    f.write(f"{i}: {ints[i]}\n")

f.close()

