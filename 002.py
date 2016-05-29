
n = 4000000
a = 1
b = 1
s = 0

while True:
    a, b = b, a + b
    if b % 2 == 0:
        s = s + b
    if b > n:
        break

print(s)
