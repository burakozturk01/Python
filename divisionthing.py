Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
0o111111
37449
37448/8
4681.0

8+64+512+4096
4680
6669566956999655695695//84
79399606630948282091
6669566956999655695695/84
7.939960663094827e+19
6669566956999655695695%84
51
51/84
0.6071428571428571
79399606630948282091+0.6071428571428571
7.939960663094827e+19
7.939960663094827e+19
7.939960663094827e+19
e+10
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    e+10
NameError: name 'e' is not defined
0.0e+10
0.0
1e+10
10000000000.0
1e+10//1
10000000000.0
1e+10//2
5000000000.0
int(1e+10)
10000000000
1e+(1e+10)
SyntaxError: invalid decimal literal
1e+10
10000000000.0
1e+1000
inf
1e+308
1e+308
1e+309
inf
0**0
1
9/0
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    9/0
ZeroDivisionError: division by zero

9.0/0
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    9.0/0
ZeroDivisionError: float division by zero
9/0.0
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    9/0.0
ZeroDivisionError: float division by zero
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    yield "."
    if a:
        for _ in range(8):
            a *= 10
            while a < b:
                a *= 10
                yield "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            yield str(i)
            if not a:
                break

            
d = div(10,3)
for a in d:
    print(a)

    
3
.
3
3
3
3
3
3
3
3
for a in div(3,0):
    print(a)

    
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    for a in div(3,0):
  File "<pyshell#39>", line 5, in div
    while a >= b:
KeyboardInterrupt
for a in div(3,3):
    print(a)

    
1
.
for a in div(3,3):
    print(a)

    
1
.
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
    
        for _ in range(8):
            a *= 10
            while a < b:
                a *= 10
                yield "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            yield str(i)
            if not a:
                break

            
for a in div(3,3):
    print(a)

    
1
for a in div(6,3):
    print(a)

    
2
for a in div(6,3):
    print(a,end="")

    
2

for a in div(100,5):
    print(a,end="")

    
20
for a in div(22,7):
    print(a,end="")

    
3.14285714
for a in div(3.14,4.5):
    print(a,end="")

    
0.69777777
3.14/4.5
0.6977777777777778
def div(x,y,prec=8):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."

        for _ in range(prec):
            a *= 10
            while a < b:
                a *= 10
                yield "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            yield str(i)
            if not a:
                break

            
for a in div(3.14,4.5):
    print(a,end="")

    
0.69777777
for a in div(3.14,4.5,100):
    print(a,end="")

    
0.697777777777777825147293495117790169186062282986111111111111111111111111111111111111111111111111111111
for a in div(314,450,100):
    print(a,end="")

    
0.6977777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
for a in div(100,100):
    print(a,end="")

    
1
def x(a,b,c=8):
    for a in div(a,b,c):
        print(a,end="")

        
x(3,4,5)
0.75
x(3,7,5)
0.42857
x(3,7,50)
0.42857142857142857142857142857142857142857142857142
x(2,41,50)
0.048780487804878048780487804878048780487804878048780487804878048
def x(a,b):
    s1 = ""
    for a in div(a,b):
        s1 += a
    if not "." in s1:
        print(s1)
    else
    
SyntaxError: expected ':'


a = 3
b = 4
c = set()
(a,b) in c
False
c.add((a,b))
c
{(3, 4)}
(a,b) in c
True
del a,b,c
div
<function div at 0x0000021E40EA2B90>
def div(x,y,prec=8):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        for _ in range(prec):
            a *= 10
            while a < b:
                a *= 10
                yield "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            yield str(i)
            if not a:
                break
            if a in states:
                print("r")
                break

            
x(10,3)
3.3r
x(22,7,30)
3.142857r
x(22,7,300)
3.142857r
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        while 1:
            a *= 10
            while a < b:
                a *= 10
                yield "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            yield str(i)
            if not a:
                break
            if a in states:
                print("r")
                break

            
def x(a,b):
    for a in div(a,b):
        print(a,end="")

        
x(22,7)
3.142857r
x(21,7)
3
x(16,80)
0.2
x(17,80)
0.2125
x(17,78)
0.2179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487179487Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    x(17,78)
  File "<pyshell#114>", line 3, in x
    print(a,end="")
KeyboardInterrupt
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        while 1:
            a *= 10
            while a < b:
                a *= 10
                yield "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            yield str(i)
            if not a:
                break
            if a in states:
                print("r")
                break
            states.add(a)

            
x(17,78)
0.2179487r
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        while 1:
            a *= 10
            while a < b:
                a *= 10
                yield "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            yield str(i)
            if not a:
                break
            if a in states:
                yield("r")
                if onemore:
                    break
                else:
                    onemore = True
                continue
            states.add(a)

            
x(17,78)
0.2179487r1r
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        while 1:
            a *= 10
            while a < b:
                a *= 10
                yield "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            yield str(i)
            if not a:
                break
            if a in states:
                yield("r")
                if onemore:
                    break
                else:
                    states = set()
                    onemore = True
                continue
            states.add(a)

            
x(17,78)
0.2179487r1794871r
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        while 1:
            a *= 10
            while a < b:
                a *= 10
                yield "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            yield str(i)
            if not a:
                break
            if a in states:
                yield("r")
                break
            states.add(a)

            
x(17,78)
0.2179487r
x(1,100)
0.01
x(441,17)
25.9411764705882352r
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += "r"
                yield s[0:len(s) - len(states)]
                yield "r"
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
x(17,78)
0.2r179487r
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")"
                yield s[0:len(s) - len(states)]
                yield "r("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
x(17,78)
0.2r(179487)
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
x(17,78)
0.21(79487)r
x(441,17)
25.941(1764705882352)r
x(4*41,17.54)
9.Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    x(4*41,17.54)
  File "<pyshell#114>", line 2, in x
    for a in div(a,b):
  File "<pyshell#142>", line 33, in div
    states.add(a)
KeyboardInterrupt
x(4.41,17.54)
0.Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    x(4.41,17.54)
  File "<pyshell#114>", line 2, in x
    for a in div(a,b):
  File "<pyshell#142>", line 27, in div
    if a in states:
KeyboardInterrupt
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
float.as_integer_ratio()
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    float.as_integer_ratio()
TypeError: unbound method float.as_integer_ratio() needs an argument
(3.5).as_integer_ratio()
(7, 2)
(3.5).as_integer_ratio()[1]
2
def div(x,y):
    a = x
    b = y
    if isinstance(a, float):
        ad = a.as_integer_ratio()[1]
        if isinstance(b, float):
            bd = b.as_integer_ratio()[1]
        else:
            bd = 1
    if isinstance(b, float):
        bd = b.as_integer_ratio()[1]
        ad = 1
    a *= ad*bd
    b *= ad*bd
    a = int(a)
    b = int(b)
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
x(4.41,17.54)
0.Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    x(4.41,17.54)
  File "<pyshell#114>", line 2, in x
    for a in div(a,b):
  File "<pyshell#153>", line 28, in div
    while 1:
KeyboardInterrupt
def divt(x,y):
    a = x
    b = y
    if isinstance(a, float):
        ad = a.as_integer_ratio()[1]
        if isinstance(b, float):
            bd = b.as_integer_ratio()[1]
        else:
            bd = 1
    if isinstance(b, float):
        bd = b.as_integer_ratio()[1]
        ad = 1
    a *= ad*bd
    b *= ad*bd
    a = int(a)
    b = int(b)
    return (a,b)

divt(4.41,17.54)
(620652323646996, 2468535545752453)
def divt(x,y):
    a = x
    b = y
    if isinstance(a, float):
        ad = a.as_integer_ratio()[1]
        if isinstance(b, float):
            bd = b.as_integer_ratio()[1]
        else:
            bd = 1
    elif isinstance(b, float):
        bd = b.as_integer_ratio()[1]
        ad = 1
    a *= ad*bd
    b *= ad*bd
    a = int(a)
    b = int(b)
    return (a,b)

divt(4.41,17.54)
(174698098343952870023263944704, 694830985250098206918383239168)
def divt(x,y):
    a = x
    b = y
    ad = 1
    bd = 1
    if isinstance(a, float):
        ad = a.as_integer_ratio()[1]
    if isinstance(b, float):
        bd = b.as_integer_ratio()[1]
    print(ad,bd)
    a *= (ad*bd)
    b *= (ad*bd)
    print(a,b)
    a = int(a)
    b = int(b)
    print(a,b)

    
divt(4.41,17.54)
281474976710656 140737488355328
1.7469809834395287e+29 6.948309852500982e+29
174698098343952870023263944704 694830985250098206918383239168
def div(x,y):
    a = x
    b = y
    ad = 1
    bd = 1
    if isinstance(a, float):
        ad = a.as_integer_ratio()[1]
    if isinstance(b, float):
        bd = b.as_integer_ratio()[1]
    a *= (ad*bd)
    b *= (ad*bd)
    a = int(a)
    b = int(b)
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
divt(4.41,17.54)
281474976710656 140737488355328
1.7469809834395287e+29 6.948309852500982e+29
174698098343952870023263944704 694830985250098206918383239168
del divt
div(4.41,17.54)
<generator object div at 0x0000021E40EB4740>
x(4.41,17.54)
0.Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    x(4.41,17.54)
  File "<pyshell#114>", line 2, in x
    for a in div(a,b):
  File "<pyshell#166>", line 37, in div
    if a in states:
KeyboardInterrupt
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
import math as m
def div(x,y):
    a = x
    b = y
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
del m
del math
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    del math
NameError: name 'math' is not defined
def div(x,y):
    a = x
    b = y
    while (a % 1 > 0.00001) or (b % 1 > 0.00001):
        a *= 10
        b *= 10
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
x(4.41,17.54)

def div(x,y):
    a = x
    b = y
    while (a % 1 > 0.00001) or (b % 1 > 0.00001):
        a *= 10
        b *= 10
    a = int(a)
    b = int(b)
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
x(4.41,17.54)
0.Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    x(4.41,17.54)
  File "<pyshell#114>", line 2, in x
    for a in div(a,b):
  File "<pyshell#182>", line 32, in div
    if a in states:
KeyboardInterrupt
def div(x,y):
    a = x
    b = y
    while (a % 1 > 0.00001) or (b % 1 > 0.00001):
        a *= 10
        b *= 10
    print(a,b)
    a = int(a)
    b = int(b)
    print(a,b)
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
x(4.41,17.54)
4410000000000000.0 1.7539999999999998e+16
4410000000000000 17539999999999998
0.Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    x(4.41,17.54)
  File "<pyshell#114>", line 2, in x
    for a in div(a,b):
  File "<pyshell#185>", line 34, in div
    if a in states:
KeyboardInterrupt
def div(x,y):
    a = x
    b = y
    while (a % 1 > 0.001) or (b % 1 > 0.001):
        a *= 10
        b *= 10
    print(a,b)
    a = int(a)
    b = int(b)
    print(a,b)
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
x(4.41,17.54)
4410000000000000.0 1.7539999999999998e+16
4410000000000000 17539999999999998
0.Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    x(4.41,17.54)
  File "<pyshell#114>", line 2, in x
    for a in div(a,b):
  File "<pyshell#188>", line 22, in div
    while 1:
KeyboardInterrupt
def div(x,y):
    a = x
    b = y
    while (a % 1 > 0.001) or (b % 1 > 0.001):
        a *= 10
        b *= 10
    print(a,b)
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
x(4.41,17.54)

def x(a,b):
    for a in div(a,b):
        print(a)

        
x(4.41,17.5)
441.0 1750.0
0
.
def x(a,b):
    for a in div(a,b):
        print(a,end="")

        
x(4.41,17.5)
441.0 1750.0
0.
def div(x,y):
    a = x
    b = y
    while (a % 1 > 0.001) or (b % 1 > 0.001):
        a *= 10
        b *= 10
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
str(3.4)
'3.4'
str(0.0)
'0.0'
str(3.400)
'3.4'
str(3.00)
'3.0'
float('3.0')
3.0
int("33")
33
3.1%1
0.10000000000000009
3.0%1
0.0
def div(x,y):
    a = x
    b = y
    if (a % 1 > 0) and (b % 1 > 0):
        sa = str(a)
        sb = str(b)
        while 1:
            if sa[-1] == "." and sb[-1] == ".":
                break
            elif sa[-1] == ".":
                sa += "0"
            elif sb[-1] == ".":
                sb += "0"
            sat = sa.split(".")
            sa = sat[0] + sat[1][0] + "." + sat[1][1:]
            sbt = sb.split(".")
            sb = sbt[0] + sbt[1][0] + "." + sbt[1][1:]
        sa += "0"
        sb += "0"
        a = int(a)
        b = int(b)
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
def divt(a,b):
    if (a % 1 > 0) and (b % 1 > 0):
        sa = str(a)
        sb = str(b)
        while 1:
            if sa[-1] == "." and sb[-1] == ".":
                break
            elif sa[-1] == ".":
                sa += "0"
            elif sb[-1] == ".":
                sb += "0"
            sat = sa.split(".")
            sa = sat[0] + sat[1][0] + "." + sat[1][1:]
            sbt = sb.split(".")
            sb = sbt[0] + sbt[1][0] + "." + sbt[1][1:]
        sa += "0"
        sb += "0"
        a = int(a)
        b = int(b)
        print(a,b)

        
def divt(a,b):
    if (a % 1 > 0) and (b % 1 > 0):
        sa = str(a)
        sb = str(b)
        while 1:
            if sa[-1] == "." and sb[-1] == ".":
                break
            elif sa[-1] == ".":
                sa += "0"
            elif sb[-1] == ".":
                sb += "0"
            sat = sa.split(".")
            sa = sat[0] + sat[1][0] + "." + sat[1][1:]
            sbt = sb.split(".")
            sb = sbt[0] + sbt[1][0] + "." + sbt[1][1:]
        sa += "0"
        sb += "0"
        a = int(a)
        b = int(b)
        print(a,b)

        
divt(3.5,42.6667)
3 42
def divt(a,b):
    if (a % 1 > 0) and (b % 1 > 0):
        sa = str(a)
        sb = str(b)
        while 1:
            if sa[-1] == "." and sb[-1] == ".":
                break
            elif sa[-1] == ".":
                sa += "0"
            elif sb[-1] == ".":
                sb += "0"
            sat = sa.split(".")
            sa = sat[0] + sat[1][0] + "." + sat[1][1:]
            sbt = sb.split(".")
            sb = sbt[0] + sbt[1][0] + "." + sbt[1][1:]
        sa += "0"
        sb += "0"
        print(a,b)
        a = int(a)
        b = int(b)
        print(a,b)

        
divt(3.5,42.6667)
3.5 42.6667
3 42
def divt(a,b):
    if (a % 1 > 0) and (b % 1 > 0):
        sa = str(a)
        sb = str(b)
        while 1:
            if sa[-1] == "." and sb[-1] == ".":
                break
            elif sa[-1] == ".":
                sa += "0"
            elif sb[-1] == ".":
                sb += "0"
            sat = sa.split(".")
            sa = sat[0] + sat[1][0] + "." + sat[1][1:]
            sbt = sb.split(".")
            sb = sbt[0] + sbt[1][0] + "." + sbt[1][1:]
        print(sa,sb)
        sa += "0"
        sb += "0"
        print(a,b)
        a = int(a)
        b = int(b)
        print(a,b)

        
divt(3.5,42.6667)
35000. 426667.
3.5 42.6667
3 42
def divt(a,b):
    if (a % 1 > 0) and (b % 1 > 0):
        sa = str(a)
        sb = str(b)
        while 1:
            if sa[-1] == "." and sb[-1] == ".":
                break
            elif sa[-1] == ".":
                sa += "0"
            elif sb[-1] == ".":
                sb += "0"
            sat = sa.split(".")
            sa = sat[0] + sat[1][0] + "." + sat[1][1:]
            sbt = sb.split(".")
            sb = sbt[0] + sbt[1][0] + "." + sbt[1][1:]
        print(sa,sb)
        sa += "0"
        sb += "0"
        print(sa,sb)
        a = int(sa)
        b = int(sb)
        print(a,b)

        
divt(3.5,42.6667)
35000. 426667.
35000.0 426667.0
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    divt(3.5,42.6667)
  File "<pyshell#224>", line 20, in divt
    a = int(sa)
ValueError: invalid literal for int() with base 10: '35000.0'
def divt(a,b):
    if (a % 1 > 0) and (b % 1 > 0):
        sa = str(a)
        sb = str(b)
        while 1:
            if sa[-1] == "." and sb[-1] == ".":
                break
            elif sa[-1] == ".":
                sa += "0"
            elif sb[-1] == ".":
                sb += "0"
            sat = sa.split(".")
            sa = sat[0] + sat[1][0] + "." + sat[1][1:]
            sbt = sb.split(".")
            sb = sbt[0] + sbt[1][0] + "." + sbt[1][1:]
        print(sa,sb)
        sa += "0"
        sb += "0"
        print(sa,sb)
        a = int(float(sa))
        b = int(float(sb))
        print(a,b)

        
divt(3.5,42.6667)
35000. 426667.
35000.0 426667.0
35000 426667
def div(x,y):
    a = x
    b = y
    if (a % 1 > 0) or (b % 1 > 0):
        a = str(a)
        b = str(b)
        while 1:
            if a[-1] == "." and b[-1] == ".":
                break
            elif a[-1] == ".":
                a += "0"
            elif b[-1] == ".":
                b += "0"
            at = a.split(".")
            a = at[0] + at[1][0] + "." + at[1][1:]
            bt = b.split(".")
            b = bt[0] + bt[1][0] + "." + bt[1][1:]
        a += "0"
        b += "0"
        a = int(float(a))
        b = int(float(b))
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
a = 0.0
str(a)
'0.0'
divt(35.0,42.0)
x(35.0,42.0)
0.83()r
x(35,42)
0.83()r
def div(x,y):
    a = x
    b = y
    if (a % 1 > 0) or (b % 1 > 0):
        a = str(a)
        b = str(b)
        while 1:
            if a[-1] == "." and b[-1] == ".":
                break
            elif a[-1] == ".":
                a += "0"
            elif b[-1] == ".":
                b += "0"
            at = a.split(".")
            a = at[0] + at[1][0] + "." + at[1][1:]
            bt = b.split(".")
            b = bt[0] + bt[1][0] + "." + bt[1][1:]
        a += "0"
        b += "0"
        a = int(float(a))
        b = int(float(b))
    i = 0
    while a >= b:
        a -= b
        i += 1
    yield str(i)
    if a:
        yield "."
        states = set()
        states.add(a)
        onemore = False
        s = ""
        while 1:
            a *= 10
            while a < b:
                a *= 10
                s += "0"
            i = 0
            while a >= b:
                a -= b
                i += 1
            s += str(i)
            if not a:
                break
            if a in states:
                if len(s) == 1:
                    break
                s += ")r"
                yield s[0:len(s) - len(states)]
                yield "("
                yield s[len(s) - len(states):]
                break
            states.add(a)

            
x(35,42)
0.83()r
