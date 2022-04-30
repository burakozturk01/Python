import random, string

def searchFor(obj, lis):
        if len(lis) == 0:
            return False
        elif len(lis) == 1:
            found = lis[0] == obj
            return found
        else:
            x = lis[:len(lis)//2]
            xl = len(x)
            
            y = lis[len(lis)//2:]
            yl = len(y)

            xr = searchFor(obj, x)
            yr = searchFor(obj, y)

            if type(xr) == bool and xr:
                return 0
            elif type(yr) == bool and yr:
                return 1
            elif type(xr) == int:
                return xr
            elif type(yr) == int:
                return yr + xl
            else:
                return False

def print_list(lis):
    for a, b in enumerate(lis):
        tmp2 = str(b)
        tmp1 = str(a)
        while len(str(tmp1)) < 3:
            tmp1 = " " + tmp1
        while len(str(tmp2)) < 20:
            tmp2 = " " + tmp2
        element = tmp1 + " - " + tmp2
        print(element, end=" | ")
        if (a+1) % 8 == 0:
            print()

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return (result_str)


lis = []

for _ in range(500):
    lis.append(get_random_string(random.randint(0, 20)))

print_list(lis)

finished = False

while not finished:

    st = input("\nSearch for?\n")

    found = searchFor(st, lis)

    if type(found) == int:
        print("Found")
        print(found, lis.pop(found))
    elif found == False:
        print("Not found")
        tmp3 = input("Wanna quit: t/f")
        finished = tmp3 == "t"




    



        

