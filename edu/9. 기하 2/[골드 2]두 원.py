import math

x1, y1, r1, x2, y2, r2 = map(float, input().split())
d = ((x1-x2)**2 + (y1-y2)**2)**0.5

r_min = min(r1, r2)
r_max = max(r1, r2)

if d <= abs(r1 - r2):
    result = math.pi * (r_min ** 2)

elif d >= r1 + r2:
    result = 0
else:
    d2 = d**2
    r1_2 = r1**2
    r2_2 = r2**2
    result = r1**2*math.acos((d2+r1_2-r2**2)/(2*d*r1))+r2**2*math.acos((d2+r2_2-r1**2)/(2*d*r2))-((-d+r1+r2)*(d+r1-r2)*(d-r1+r2)*(d+r1+r2))**0.5*0.5

print("{:.3f}".format(result))
