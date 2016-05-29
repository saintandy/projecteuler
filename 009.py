
import math

def IsPerfectSquare(n):
    if pow(int(math.sqrt(n)), 2) == n:
        return True
    return False

for i in range(1, 1001):
    for j in range(1, 1001):
        if IsPerfectSquare(i * i + j * j):
            if i + j + math.sqrt(i * i + j * j) == 1000:
                print i * j * math.sqrt(i * i + j * j)

