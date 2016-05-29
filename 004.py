
def IsPalindrome(n):
    d = n
    c = 0
    while n > 0:
        c = c * 10 + n % 10;
        n = n / 10
    if d == c:
        return True
    return False

r = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if IsPalindrome(i * j):
            r = max(r, i * j)

print r
