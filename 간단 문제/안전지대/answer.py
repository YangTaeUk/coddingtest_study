def solution(board):
    answer = 0
    sizeOfboard1 = len(board)
    sizeOfboard2 = len(board[0])

    # 이동 방향 리스트 (상하좌우 및 대각선 포함)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # 상, 하, 좌, 우
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # 대각선 방향
    ]

    # 주변을 2로 표시
    for i in range(sizeOfboard1):
        for j in range(sizeOfboard2):
            if board[i][j] == 1:
                board[i][j] = 2  # 현재 위치를 2로 변경
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < sizeOfboard1 and 0 <= nj < sizeOfboard2:
                        if board[ni][nj] == 0 : board[ni][nj] = 2
    # 안전지대 개수 세기
    for i in range(sizeOfboard1):
        for j in range(sizeOfboard2):
            if board[i][j] == 0:
                answer += 1

    return answer

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
];

print (solution(board));
