from pprint import pprint
def solution(n, results):
    answer = 0

    score = [[0 for i in range(n)] for i in range(n)]

    for result in results:
        score[result[0]-1][result[1]-1] = 1
        score[result[1]-1][result[0]-1] = -1
    pprint("----------------------")
    pprint(score)

    for k in range(n): # 중간
        for i in range(n): # 시작
            for j in range(n): # 끝
                # 논리적으로 맞는것만 체크해야 하니까
                if score[i][k] == 1 and score[k][j] == 1:
                    score[i][j] = 1
                elif score[i][k] == -1 and score[k][j] == -1:
                    score[i][j] = -1
    pprint("----------------------")
    pprint(score)
    pprint("----------------------")
    for i in range(n):
        count = 0
        for j in range(n):
            if score[i][j] != 0:
                count += 1
            if i == j and score[i][j] == 0:
                count += 1
        if 5 == count: answer += 1

    return answer

n= 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
pprint(solution(n ,results))