import sys
data = sys.stdin.readlines()
for num in data[1:]:
    num = bin(int(num)).replace("0b","")
    print(" ".join([str(index) for index, s in enumerate(num[::-1]) if s == "1"]))