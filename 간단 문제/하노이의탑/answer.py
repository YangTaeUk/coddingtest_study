import pprint
def solution(n):
    answer = []
    def move(num, start, end):
        answer.append([start, end])

    def hanoi(num, start, end, sub):
        if num == 1 :
            move(num, start, end)
        else:
            hanoi(num - 1, start, sub, end)
            move(num, start, end)
            hanoi(num - 1, sub, end, start)

    hanoi(n, 1, 3, 2)
    return answer
pprint.pprint(solution(2))








