from collections import deque


def count_differences(word1, word2):
    # 각 위치의 문자를 비교하여 다른 개수를 셉니다.
    difference_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return difference_count

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    else:
        wordlen = len(words)
        visit = set()  # 시작점을 방문한 상태로 초기화
        # 큐 초기화
        q = deque([(-1, 1)])  # (words의 index, 현재까지의 거리)
        while q:
            wordindex, step = q.popleft()  # 큐의 맨 앞 요소를 꺼내 wordindex, step에 할당
            if wordindex != -1 :
                if words[wordindex] == target:
                    return step
            for i in range(wordlen):
                difcount = count_differences(begin, words[i])
                if difcount == 1 and words[i] not in visit:
                    print(words[i])
                    begin = words[i]
                    q.append((i, step + 1))
                    visit.add(i)
        return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))