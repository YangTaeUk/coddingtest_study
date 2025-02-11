import re

def solution(s):
    answer = []
    stringA = s.split(" ")
    for stringa in stringA:
        stringa = stringa.lower()
        pattern = r"^[A-Za-z]"

        if re.match(pattern, stringa):
            stringa = stringa[0].upper() + stringa[1:]

        answer.append(stringa)
    return " ".join(answer)

print(solution("3people unFollowed me"))
