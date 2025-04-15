import sys, math
data = sys.stdin.readlines()
a,b = map(int, data[0].strip().split())
g = math.gcd(a,b)
print(g)
print(int(a*b/g))