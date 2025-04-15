import sys
data = sys.stdin.readlines()
n = int(data[0].strip())
arr = list(list(d.strip().split() for d in data[1:]))
#
# for i in range(n):
#     for j in range(n):
