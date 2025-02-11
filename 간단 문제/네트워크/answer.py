
def DFS(n, computers, com, visited):
    visited[com] = True        # 해당 노드의 방문 여부를 True로 변경
    for i in range(n):          # 해당 노드와 연결된 다음 노드들을 모두 탐색
        if i != com and computers[i][com] == 1 and visited[i] == False:
                DFS(n, computers, i, visited)       # i랑 연결된 다음 노드도 쭉 탐색

def solution(n, computers):
    answer = 0
    visit = [0 for i in range(n)]
    for i in range(n):
        if visit[i] == 0:
            DFS(n, computers, i, visit)
            answer += 1
    return answer


n = 3
computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n,computers1))
print(solution(n,computers2))