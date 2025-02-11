import sys
data = sys.stdin.read().splitlines()

x1,y1,x2,y2 = map(int, data[0].split())
x3,y3,x4,y4 = map(int, data[1].split())

def ccw(p1_x,p1_y,p2_x,p2_y,p3_x,p3_y):
    return (p2_x - p1_x) * (p3_y - p1_y) - (p2_y - p1_y)*(p3_x - p1_x)


def cross_check():
    ccw1 = ccw(x1,y1,x2,y2,x3,y3)
    ccw2 = ccw(x1,y1,x2,y2,x4,y4)
    ccw3 = ccw(x3,y3,x4,y4,x1,y1)
    ccw4 = ccw(x3,y3,x4,y4,x2,y2)

    if ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0:
        return 1

    def is_between(a,b,c):
        return min(a,b)<=c<=max(a,b)

    if ccw1 == 0 and is_between(x1, x2, x3) and is_between(y1, y2, y3):
        return 1
    if ccw2 == 0 and is_between(x1, x2, x4) and is_between(y1, y2, y4):
        return 1
    if ccw3 == 0 and is_between(x3, x4, x1) and is_between(y3, y4, y1):
        return 1
    if ccw4 == 0 and is_between(x3, x4, x2) and is_between(y3, y4, y2):
        return 1

    return 0  # 교차하지 않음
print(cross_check())