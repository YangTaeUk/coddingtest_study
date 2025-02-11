import sys
def get_segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4):

    return 0

data = sys.stdin.read().splitlines()
x1, y1, x2, y2 = map(int, data[0].split())
x3, y3, x4, y4 = map(int, data[1].split())
result = get_segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4)

if isinstance(result, tuple):
    print(1)
    print(result[0], result[1])
else:
    print(result)
