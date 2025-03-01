# def compute_lps(pattern):
#     m = len(pattern)
#     lps = [0] * m
#     length = 0
#     i = 1
#     while i < m:
#         if pattern[i] == pattern[length]:
#             length += 1
#             lps[i] = length
#             i += 1
#         else:
#             if length != 0:
#                 length = lps[length-1]
#             else:
#                 lps[i] = 0
#                 i += 1
#     return lps
# def kmp_search(text, pattern):
#     n = len(text)
#     m = len(pattern)
#     lps = compute_lps(pattern)
#     i = 0
#     j = 0
#     positions = []
#     while i < n:
#         if text[i] == pattern[j]:
#             i += 1
#             j += 1
#         if j == m:
#             positions.append(i - j + 1)
#             j= lps[j - 1]
#         elif i < n and text[i] != pattern[j]:
#             if j != 0:
#                 j = lps[j - 1]
#             else:
#                 i += 1
#
#     return positions
#
# import sys
# data = sys.stdin.readlines()
# T = data[0].strip('\n')
# P = data[1].strip('\n')
# result = kmp_search(T, P)
# length = len(result)
# if length != 0:
#     print(length)
#     print(" ".join(str(r) for r in result))
# else:
#     print(length)
#

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m > n:
        return []

    base = 256
    mod = 101  # 임의의 소수
    h = 1
    p_hash = 0
    t_hash = 0
    positions = []

    # h = pow(base, m-1) % mod
    for i in range(m - 1):
        h = (h * base) % mod

    # 초기 패턴과 텍스트의 첫 윈도우 해시 계산
    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % mod
        t_hash = (base * t_hash + ord(text[i])) % mod

    # 텍스트 전체에 대해 슬라이딩 윈도우 적용
    for i in range(n - m + 1):
        # 패턴의 해시와 현재 텍스트 윈도우의 해시가 같으면 실제 문자열 비교
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                positions.append(i+1)

        # 다음 윈도우 해시 계산: 롤링 해시 방식
        if i < n - m:
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            if t_hash < 0:
                t_hash += mod

    return positions

import sys
data = sys.stdin.readlines()
T = data[0].strip('\n')
P = data[1].strip('\n')
result = rabin_karp(T, P)
length = len(result)
if length != 0:
    print(length)
    print(" ".join(str(r) for r in result))
else:
    print(length)