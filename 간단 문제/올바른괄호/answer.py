def solution(s):
    if (s.startswith(")") or s.endswith("(")):
        return False
    elif s.count("(") != s.count(")"):
        return False
    else:
        stack = []
        for i in s:
            if i == '(':  # '('는 stack에 추가
                stack.append(i)
            else:  # i == ')'인 경우
                if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
                    return False
                else:
                    stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거
        return stack == []

s="((((())))"
print(solution(s))