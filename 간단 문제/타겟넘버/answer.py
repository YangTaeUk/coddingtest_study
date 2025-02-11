def solution(numbers, target):
    answer = 0
    lennum = len(numbers)
    allanswer = [0]

    for num in numbers:
        temp = []
        for an in allanswer:
            temp.append(an + num)
            temp.append(an - num)
        allanswer = temp

    for a in allanswer:
        if a == target:
            answer += 1
    return answer

numbers = [1, 2, 3, 4, 5]
target = 3
print(solution(numbers, target))