import math as m
def primes(begin, end):
        plist = [2]
        #print(f"beginning, primes:{plist}")
        for i in range(3, end + 1):
                #print(f"checking number {i}")
                prime = True
                for j in plist:
                        #print(f"Checking for prime {j}")
                        if i % j == 0:
                                prime = False
                                break
                        elif j*j > i:
                                break
                #print(f"Is i prime? {prime}")
                if prime:
                        plist.append(i)
                #print(f"Updated list: {plist}")
        plist_  = []
        for p in plist:
                if begin <= p:
                        if p > end:
                                break
                        plist_.append(p)
        plist = plist_
        return plist

print(primes(0,int(input())))
