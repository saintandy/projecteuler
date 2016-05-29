
# how do I do this in the functional way? I mean haskell-like

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

r = 1;

for i in range(1, 21):
    r = lcm(r, i)

print r
