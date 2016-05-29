
n = 2000001
r = 0
sieve = []

for i in range(0, n):
    sieve.append(False)

for i in range(2, n):
    if sieve[i] == False:
        for j in range(i * i, n, i):
            sieve[j] = True

for i in range(2, n):
    if sieve[i] == False:
        r = r + i

print r
