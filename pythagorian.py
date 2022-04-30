import random

class Triangle:
    def __init__(self, *args):

        if len(args) == 3:
            x = args[0]
            y = args[1]
            self.a = min(x, y)
            self.b = max(x, y)
            self.c = args[2]

        elif len(args) == 2:
            x = args[1] ** 2 - args[0] ** 2
            y = 2 * args[0] * args[1]
            self.c = args[0] ** 2 + args[1] ** 2
            self.a = min(x, y)
            self.b = max(x, y)

        else:
            raise Exception("Must have 2 or 3 args")

    def __repr__(self):
        return f"{self.a} - {self.b} - {self.c}\nArea: {self.getArea()} br^2 | Circum: {self.getCircum()} br\n"

    def __gt__(self, other):
        return self.c > other.c

    def getArea(self):
        return int(self.a * self.b / 2)

    def getCircum(self):
        return self.a + self.b + self.c

    @classmethod
    def min(cls, t1, t2):
        if t1.c < t2.c:
            return t1
        else:
            return t2

    def dims(self):
        return self.a, self.b

    def draw(self):
        x, y = self.dims()
        st = ""

        for b in range(y):
            for a in range(round(b * x / y)):
                st += "* "
            st += "\n"
        return st


class PhyTris:
    def __init__(self, r):
        ind = 0
        self.tris = []
        same = False

        if r < 3:
            r = 3

        for m in range(1, r):
            for n in range(m + 1, r + 1):
                tmp = Triangle(m, n)
                for i in range(len(self.tris)):
                    if tmp.a / self.tris[i].a == tmp.c / self.tris[i].c:
                        same = True
                        ind = i
                if same:
                    tmp2 = self.tris.pop(ind)
                    self.tris.append(Triangle.min(tmp2, tmp))
                    same = True
                else:
                    self.tris.append(tmp)
                same = False
        self.sort()

    def __repr__(self):
        s = "a - b - c\nSize / Circum\n\n"

        for tri in self.tris:
            s += tri.__repr__() + "\n"

        return s

    def __len__(self):
        return len(self.tris)

    def sort(self):
        finished = False
        j = 0

        while not finished:
            for i in range(j, len(self.tris) - 1):
                if self.tris[i] > self.tris[i + 1]:
                    tmp3 = self.tris[i]
                    self.tris[i] = self.tris[i + 1]
                    self.tris[i + 1] = tmp3
                    j = i - 1
                    if j < 0:
                        j = 0
                    break
                if i == len(self.tris) - 2:
                    finished = True

    def getTri(self, index):
        return self.tris[index]

    def getLastInd(self):
        return len(self.tris) - 1


inp1 = input("Please enter an positive \"range\" integer\n")
inp1 = int(inp1)
if inp1 > 0:
    list1 = PhyTris(inp1)
    print(f"{len(list1)} phytagorian triangle(s) generated.")

    inp1 = input("Do you wanna see examples from start, end or randomly choosen?\n(start, end, random)\n")
    inp1.lower()
    inp2 = input("How many examples do you wanna see?\n")
    inp2 = int(inp2)
    if 0 < inp2 <= len(list1):
        if inp1 == "start":
            for i in range(inp2):
                print(list1.getTri(i))
        elif inp1 == "end":
            for i in range(len(list1) - inp2, len(list1)):
                print(list1.getTri(i))
        elif inp1 == "random":
            for _ in range(inp2):
                print(list1.getTri(round(random.uniform(0, len(list1) - 1))))
        else:
            print("Invalid input")
    else:
        print("Invalid input")
else:
    print("Invalid input")

input()
