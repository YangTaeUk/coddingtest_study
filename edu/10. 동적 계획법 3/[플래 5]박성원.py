import sys
import math

def probability_of_text_subsets(n, set_arr, k):
    # 1️⃣ 각 숫자의 K에 대한 나머지를 미리 계산
    mod_list = [int(num) % k for num in set_arr]
    length_list = [len(num) for num in set_arr]

    # 2️⃣ 10^len(num) % k 값을 미리 계산 (연결할 때 활용)
    power_mod = [1] * 51
    for i in range(1, 51):
        power_mod[i] = (power_mod[i - 1] * 10) % k

    # 3️⃣ DP 테이블 초기화 (dp[bit][mod] -> 해당 상태가 가능한지 여부 저장)
    dp = [[0] * k for _ in range(1 << n)]
    dp[0][0] = 1  # 시작 상태 (아무 숫자도 선택하지 않음)

    # 4️⃣ 비트마스킹 + DP 수행
    for bit in range(1 << n):
        for mod in range(k):
            if dp[bit][mod] == 0:  # 현재 상태가 존재하지 않으면 스킵
                continue

            for i in range(n):
                if bit & (1 << i):  # 이미 사용한 숫자면 스킵
                    continue

                # 새로운 비트마스크 상태
                new_bit = bit | (1 << i)

                # 새로운 나머지 계산
                new_mod = (mod * power_mod[length_list[i]] + mod_list[i]) % k

                # dp 갱신
                dp[new_bit][new_mod] += dp[bit][mod]

    # 5️⃣ 가능한 경우의 수 구하기
    total_permutations = math.factorial(n)
    valid_permutations = dp[(1 << n) - 1][0]  # 모든 숫자를 사용하고 나머지가 0인 경우의 수

    # 6️⃣ 기약분수 형태로 변환하여 출력
    if valid_permutations == 0:
        print("0/1")
    elif valid_permutations == total_permutations:
        print("1/1")
    else:
        gcd_value = math.gcd(valid_permutations, total_permutations)
        print(f"{valid_permutations // gcd_value}/{total_permutations // gcd_value}")


# ✅ 입력 처리
input_text = sys.stdin.read()
data = input_text.splitlines()
n = int(data[0])
set_arr = [d.strip() for d in data[1:-1]]
k = int(data[-1])

# ✅ 실행
probability_of_text_subsets(n, set_arr, k)
