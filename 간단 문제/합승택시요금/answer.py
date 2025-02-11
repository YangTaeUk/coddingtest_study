import pprint

def solution(n, start, ahouse, bhouse, fares):
    answer = 1000000000
    irange = range(0, n)
    jrange = range(0, n)
    krange = range(0, n)
    matrixA = [[0 for col in range(n)] for i in range(n)]
    for i in irange:
        for j in jrange:
            if i == j: matrixA[i][j] = 0;
            else: matrixA[i][j] = 1000000000
    for fare in fares:
        matrixA[fare[0]-1][fare[1]-1] = fare[2]
        matrixA[fare[1]-1][fare[0]-1] = fare[2]

    for k in krange:
        for i in irange:
            #answer = matrixA[i][k]
            for j in jrange:
                if matrixA[i][j] > matrixA[i][k] + matrixA[k][j]:
                    matrixA[i][j] = matrixA[i][k] + matrixA[k][j]
                # if i == start-1 and (j == ahouse-1 or j == bhouse-1):
                #     # pprint.pprint("42matrixA[" + str(i + 1) + "][" + str(j + 1) + "]:" + str(matrixA[i][j])
                #     #               + "matrixA[" + str(i + 1) + "][" + str(k + 1) + "]:" + str(matrixA[i][k])
                #     #               + "matrixA[" + str(k + 1) + "][" + str(j + 1) + "]:" + str(matrixA[k][j]))
                #     answer += matrixA[k][j]
    #         if i == start-1:
    #             pprint.pprint(answer)
    #                     # pprint.pprint(matrixA[i][j])
    #                     # pprint.pprint(matrixA[i][k])
    #                     # pprint.pprint(matrixA[k][j])
    #             #loute.append("("+str(i)+","+str(j)+")")
    #     # pprint.pprint(loute)

    answer = matrixA[start-1][ahouse-1] + matrixA[start-1][bhouse-1]
    for i in irange:
        answer = min(answer, matrixA[start-1][i] + matrixA[i][ahouse-1] + matrixA[i][bhouse-1])

    # pprint.pprint(matrixA[start-1][ahouse-1])
    # pprint.pprint(matrixA[start-1][bhouse-1])
    # pprint.pprint(matrixA)
    pprint.pprint(answer)
    return answer

n = 6
start = 4
ahouse = 6
bhouse = 2
fares =[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n, start, ahouse, bhouse, fares)

