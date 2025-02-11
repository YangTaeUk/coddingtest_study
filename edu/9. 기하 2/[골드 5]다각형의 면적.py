import sys
inputA = sys.stdin.read
data = inputA().splitlines()
n = int(data[0])
locationX = []
locationY = []
for d in data[1:]:
    x,y = map(int, d.strip().split())
    locationX.append(x)
    locationY.append(y)
locationX.append(locationX[0])
locationY.append(locationY[0])
a, b = 0, 0

for i in range(n):
    a += locationX[i] * locationY[i+1]
    b += locationY[i] * locationX[i+1]

print(round(abs(a-b)/2, 1))