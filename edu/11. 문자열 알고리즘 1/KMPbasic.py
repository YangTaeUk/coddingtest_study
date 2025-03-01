import time

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

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    position = []
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            position.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                 i += 1

    return position


# 실행 시간 측정
if __name__ == '__main__':
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    start_time = time.time()  # 시작 시간 기록
    positions = kmp_search(text, pattern)
    end_time = time.time()  # 종료 시간 기록

    print("패턴이 발견된 위치:", positions)
    print("실행 시간: {:.30f}초".format(end_time - start_time))
