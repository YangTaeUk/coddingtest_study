def solution(s):
    cnt0 = 0
    cnt = 0
    while (s != "1"):
        cnt0 += s.count("0")
        s = str(bin(int(len(s.replace("0", ""))))).replace("0b","")
        cnt += 1
    return str([cnt, cnt0])






print("110010101001 : " + solution("110010101001") )
print("01110 : " + solution("01110"))
