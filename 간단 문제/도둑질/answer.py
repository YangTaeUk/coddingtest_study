def solution(money):
    lenmoney = len(money)
    if lenmoney == 3: return max(money)
    else:
        getfirsthouse, getlasthouse = money[:], money[:]
        getfirsthouse[0]=0
        getlasthouse[1]=max(money[0],money[1])
        for i in range(2, lenmoney):
            getfirsthouse[i] = max(getfirsthouse[i-2]+getfirsthouse[i], getfirsthouse[i-1])
            if lenmoney-1>i:
                getlasthouse[i] = max(getlasthouse[i-2]+getlasthouse[i], getlasthouse[i-1])

        return max(getfirsthouse[-1], getfirsthouse[-2], getlasthouse[-1], getlasthouse[-2])

money = [1, 2, 3, 1, 5, 8]
money2 = [1, 2, 3, 4, 7]
money3 = [6, 2, 1, 2, 3, 4, 7]
money4 = [5, 1, 1, 2, 3, 4, 7]

print(solution(money))
print(solution(money2))
print(solution(money3))
print(solution(money4))
