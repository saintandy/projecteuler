
n = 1000
s = 0

for i in range(1, n):
    if i % 3 == 0:
        s = s + i
    if i % 5 == 0:
        s = s + i
    if i % 15 == 0:
        s = s - i

print s
