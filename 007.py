
import math

limit = 10001
count = 0
i = 2

def IsPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    if IsPrime(i):
        count = count + 1
        if count == limit:
            print i
            break
    i = i + 1

