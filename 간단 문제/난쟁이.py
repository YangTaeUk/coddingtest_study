from itertools import combinations
import sys

data = sys.stdin.readlines()
arr = set([int(d) for d in data if int(d) != 0])

for c in combinations(arr, 7):
    if sum(c) == 100:
        for num in sorted(c):
            print(num)
        break