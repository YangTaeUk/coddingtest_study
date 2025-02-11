import sys
inputA = sys.stdin.read
data = inputA().splitlines()
arrx = []
arry = []
for d in data:
    x,y = map(int, d.strip().split())
    arrx.append(x)
    arry.append(y)
answer = (arrx[0]*arry[1]+arrx[1]*arry[2]+arrx[2]*arry[0])-(arrx[1]*arry[0]+arrx[2]*arry[1]+arrx[0]*arry[2])
print(-1 if answer < 0 else 1 if answer > 0 else answer)