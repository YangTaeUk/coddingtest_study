def solution(n, arr1, arr2):
    arr1bin = tobin(n, arr1)
    arr2bin = tobin(n, arr2)
    answer = [];
    irange = range(0,len(arr1))
    jrange = range(0,n)

    for i in irange:
        answersub = ""
        for j in jrange:
            if arr1bin[i][j] == "1" or arr2bin[i][j] == "1":
                answersub += "#"
            else:
                answersub += " "
        answer.append(answersub)

    return answer

def tobin(n, arr):
    res = [];
    for i in arr:
        text = str(bin(i)).replace('0b', '', 1)
        for j in range(len(text), n):
            text = '0' + text
        res.append(list(text))
    return res

n = 5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]

print (solution(n, arr1, arr2));
