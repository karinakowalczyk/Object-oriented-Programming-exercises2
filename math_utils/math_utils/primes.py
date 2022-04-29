
from math import sqrt
def isprime(p):
    result = True
    if p == 1:
        result = False
    if p!=2:
        for i in range(2,int(sqrt(p))+1):
            if p % i==0:
                result = False
    return result

print(isprime(1))