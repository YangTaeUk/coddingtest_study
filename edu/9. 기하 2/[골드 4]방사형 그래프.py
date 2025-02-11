from itertools import permutations
import math

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def is_convex(arr):
    points = []
    for i in range(8):
        angle = i * 45
        rad = angle * (math.pi / 180)
        x = arr[i] * math.cos(rad)
        y = arr[i] * math.sin(rad)
        points.append((x, y))

    for i in range(8):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 8]
        x3, y3 = points[(i + 2) % 8]
        if ccw(x1, y1, x2, y2, x3, y3) <= 0:
            return False
    return True

def count_convex_permutations(abilities):
    count = 0
    for perm in permutations(abilities):
        if is_convex(perm):
            count += 1
    return count

print(count_convex_permutations(list(map(int, input().split()))))
