"""
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

"""
import sys

S = 0  # 비트마스킹으로 집합 관리

input = sys.stdin.readline  # 한 줄씩 읽기 최적화
n = int(input().strip())  # 첫 번째 줄에서 명령어 개수 읽기

for _ in range(n):
    part = input().strip().split()
    order = part[0]

    if len(part) == 2:
        num = int(part[1])
    if order == "add":
        S |= (1 << num)
    elif order == "remove":
        S &= ~(1 << num)
    elif order == "check":
        print(1 if (S & (1 << num)) else 0)
    elif order == "toggle":
        S ^= (1 << num)
    elif order == "all":
        S = (1 << 21) - 1  # 0~20까지 모든 비트 1로 설정
    elif order == "empty":
        S = 0  # 모든 비트 초기화
