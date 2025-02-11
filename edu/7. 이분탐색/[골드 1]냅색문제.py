"""
시간 제한 1초  / 메모리 제한 128 MB

문제 : 세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.
N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 N과 C가 주어진다. N은 30보다 작거나 같은 자연수, C는 10^9보다 작거나 같은 음이 아닌 정수이다. 둘째 줄에 물건의 무게가 주어진다. 무게도 10^9보다 작거나 같은 자연수이다.

가이드 :  부분 집합 합 계산 (Meet-in-the-Middle) 사용

예제 입력 1 
2 1
1 1

제한 사항 확인.
시간 제한 1초  / 메모리 제한 128 MB
N≤30 으로
모든 경우의 수
2^30=1,073,741,824

10^9번의 연산
2^30×8bytes=8GB
"""
from itertools import combinations
import sys

data = sys.stdin.readlines()
N, C  = map(int, data[0].strip().split())
arr = list(map(int, data[1].strip().split()))

def comb(arr_list):
    s = []
    for i in range(len(arr_list)+1):
        for c in combinations(arr_list, i):
            s.append(sum(c))
    return s

S1 = comb(arr[:N//2])
S2 = comb(arr[N//2:])
S2.sort()

answer = 0
for s1 in S1:
    if s1 <= C:
        left, right = 0, len(S2)
        while left < right:
            mid = (left+right) // 2
            if s1+S2[mid] <= C:
                left = mid+1
            else:
                right = mid
        answer += left

print(answer)
