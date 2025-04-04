# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/68647
# 알고리즘: DP (동적 계획법)
# 시간 복잡도: O(N^2 * M)  // N = 행의 개수, M = 열의 개수
#
# 최종 결과는 MOD = 10^7 + 19 로 나눈 나머지를 반환합니다.

MOD = 10 ** 7 + 19  # 모든 계산은 이 값으로 나눈 나머지를 사용

# 전역 변수: 조합(nCr) 값을 저장할 2차원 리스트 (메모이제이션 용도)
# 최대 n 값이 300이므로, 0 ~ 301까지 사용 (인덱스 0~301, 총 302개)
combi = [[-1] * 302 for _ in range(302)]


def getCombination(n, r):
    """
    getCombination: n개 중 r개를 선택하는 조합의 수를 MOD로 나눈 값을 구하는 함수

    매개변수:
      n : 전체 원소의 개수
      r : 선택할 원소의 개수

    반환:
      nCr (MOD로 나눈 값)
    """
    # 선택하는 개수가 전체보다 많으면 0 반환
    if n < r:
        return 0

    # 이미 계산한 값이면 바로 반환 (메모이제이션)
    if combi[n][r] != -1:
        return combi[n][r]

    # n과 r이 같거나 r이 0이면 경우의 수는 1 (기저 사례)
    if n == r or r == 0:
        combi[n][r] = 1
        return 1

    # 점화식: C(n, r) = C(n-1, r-1) + C(n-1, r)
    combi[n][r] = (getCombination(n - 1, r - 1) + getCombination(n - 1, r)) % MOD
    return combi[n][r]


def solution(arr):
    """
    solution: 주어진 0-1 행렬 arr에 대해, 각 열의 1의 개수를 유지하면서
              최종적으로 각 행의 1의 개수가 짝수가 되는 경우의 수를 구하는 함수.

    매개변수:
      arr : 입력 0-1 행렬 (리스트의 리스트)

    반환:
      조건을 만족하는 행렬의 경우의 수 (MOD로 나눈 나머지)
    """
    n = len(arr)  # 행의 개수
    m = len(arr[0])  # 열의 개수

    # 조합 계산을 위한 메모이제이션 배열을 초기화 (최대 301 x 301 크기)
    global combi
    combi = [[-1] * 302 for _ in range(302)]

    # oneCnts[j]: 입력 행렬에서 j번째 열(1-indexed)의 1의 개수를 저장
    # 인덱스를 1부터 사용하기 위해 길이 m+1의 리스트를 사용합니다.
    oneCnts = [0] * (m + 1)
    for i in range(n):
        for j in range(m):
            oneCnts[j + 1] += arr[i][j]

    """
    dp[c][num] 정의:
      - c: 현재까지 처리한 열의 개수 (0부터 m까지; 0은 아직 한 열도 처리하지 않은 상태)
      - num: 현재까지 처리한 열들에서, 1의 개수가 짝수인 행의 개수

    dp[c][num]의 값은,
      arr의 0번째 열부터 c번째 열까지 고려했을 때,
      num개의 행이 "1의 개수가 짝수"인 경우의 수를 의미합니다.

    초기 상태:
      - 아직 아무 열도 처리하지 않은 상태에서는 각 행의 1의 개수가 0이므로(짝수),
        모든 n개의 행이 짝수인 상태입니다.
        즉, dp[0][n] = 1.
    """
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][n] = 1  # 기저 사례: 열을 하나도 처리하지 않았을 때, 모든 행이 짝수(0개)임.

    # 열을 1부터 m까지 순차적으로 처리
    for col in range(1, m + 1):
        oneCnt = oneCnts[col]  # 현재 열에서 반드시 배분해야 하는 1의 개수

        # 이전 열까지 처리한 상태에서, num개의 행이 짝수인 경우를 모두 고려
        for num in range(0, n + 1):
            # 이전 상태(dp[col-1][num])가 0이면 건너뜁니다.
            if dp[col - 1][num] == 0:
                continue

            # 현재 열에서 배분할 1의 개수(oneCnt)를,
            # 기존에 짝수인 행과 홀수인 행에 배분하는 모든 경우를 시도합니다.
            # k: 기존 짝수 행 중 몇 개의 행에 1을 넣어 홀수로 바꿀지
            for k in range(0, oneCnt + 1):
                # 그러면 나머지 oneCnt - k 개의 1은 기존 홀수 행에 넣어 짝수로 바꿉니다.
                willSetOddRow = oneCnt - k

                # 새로운 짝수 행의 개수 계산:
                #   - 기존 짝수 행 중 1을 넣지 않은 행: num - k
                #   - 기존 홀수 행 중 1을 넣어 짝수로 전환된 행: willSetOddRow
                new_even = (num - k) + willSetOddRow

                # 만약 k가 현재 짝수 행의 수보다 많거나, oneCnt-k가 현재 홀수 행의 수보다 많다면 불가능
                if k > num or (oneCnt - k) > (n - num):
                    continue

                # new_even이 전체 행의 범위를 벗어나면 건너뜁니다.
                if new_even < 0 or new_even > n:
                    continue

                # 경우의 수 계산:
                #   - 기존 짝수 행 중에서 k개를 선택하는 경우의 수: C(num, k)
                #   - 기존 홀수 행 중에서 (oneCnt - k)개를 선택하는 경우의 수: C(n - num, oneCnt - k)
                ways = (getCombination(num, k) * getCombination(n - num, oneCnt - k)) % MOD

                # 현재 상태(dp[col-1][num])에서 경우의 수를 곱해 새로운 상태(dp[col][new_even])에 누적
                dp[col][new_even] = (dp[col][new_even] + dp[col - 1][num] * ways) % MOD

    # 모든 m개의 열을 처리한 후, 모든 행(총 n개)이 짝수인 경우의 수가 정답입니다.
    return dp[m][n]


# 예시 실행
if __name__ == "__main__":
    # 예시 3x3 행렬: 각 행과 열에 1이 2개씩 있어야 한다고 가정
    # (문제 조건에 따라 입력 arr가 주어집니다)
    example_arr = [
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 0]
    ]

    result = solution(example_arr)
    print("조건을 만족하는 행렬의 경우의 수 (MOD 10^7+19):", result)
