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
#                 length = lps[length - 1]
#             else:
#                 lps[i] = 0
#                 i += 1
#     return lps
#
# def kmp_search(text, pattern):
#     n = len(text)
#     m = len(pattern)
#     lps = compute_lps(pattern)
#     i = 0
#     j = 0
#     position = []
#     k = 0
#     while i < n:
#         if text[i] == pattern[j]:
#             print(i, j)
#             i += 1
#             j += 1
#             if i-1 not in position and i == n:
#                 print(i-1, position, n)
#                 i = 0
#                 if k == 1:
#                     break
#                 k += 1
#         if j == m:
#             position.append(i - j if 0 < i - j else n + i - j)
#             j = lps[j - 1]
#         elif i < n and text[i] != pattern[j]:
#             if j != 0:
#                 j = lps[j - 1]
#             else:
#                  i += 1
#
#     return position
#
#
# def compute_failure_function(pattern):
#     m = len(pattern)
#     failure = [0] * m
#     j = 0  # 접두사 포인터
#
#     for i in range(1, m):
#         while j > 0 and pattern[i] != pattern[j]:
#             j = failure[j - 1]  # 이전 접두사로 이동
#         if pattern[i] == pattern[j]:
#             j += 1
#         failure[i] = j
#
#     return failure
#
#
# if __name__ == '__main__':
#     text = "abaaba"
#     pattern = "ba"
#     print(compute_lps("ababababababab"),len("ababababababab"))
#     print(compute_lps("abababababababababababababab"),len("abababababababababababababab"))
#     print(compute_lps("abababababababk"),len("abababababababk"))
#     print(compute_lps("abababababababkabababababababk"),len("abababababababkabababababababk"))
#     print(compute_lps("abaabaabaabaaba"))
#     print(compute_lps("abbaabbaabbaabbaabba"))
#     print(compute_lps("baaabbaaabbaaabbaaab"))
#
#     # for _ in range(len(text)):
#     #     positions = kmp_search(text, pattern)
#     #     print("패턴이 발견된 위치:", positions)
#     #     pattern = pattern[:-2]
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

import sys
data = sys.stdin.readlines()
n = int(data[0].strip())
s = data[1].strip()
print(n - compute_lps(s)[-1])
