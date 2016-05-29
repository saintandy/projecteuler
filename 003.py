
import math

n = 600851475143
d = n
r = 0

len = int(math.sqrt(n))
for i in range(2, len + 1):
    if n % i == 0:
        r = max(r, i);
        while n % i == 0:
            n = n / i

r = max(r, n)

print r
