# import sys
# data = sys.stdin.readline()
# n = int(data[0].strip())
# lines = [list(map(int, line.strip().split())) for line in data[1:]]
# print(lines)
# # for k in range(n-1):
# #     print(f"Case #{k + 1}: {sum(lines[k])}")
import heapq
from bisect import bisect_left, bisect
from collections import defaultdict
from sys import modules

from django.templatetags.i18n import LanguageNode


# a, target = map(int, input().split())
# A = list(map(int, input().split()))
# answer = ""
# while A:
#     num = A.pop()
#     if num < target:
#         if answer == "":
#             answer += str(num)
#         else:
#             answer += (" "+str(num))
# print(answer)


#from collections import defaultdict
#data = sys.stdin.readlines()
#n, m = map(int, data[0].strip().split())
#lines = [list(map(int, l.strip().split())) for l in data[1:]]
# n, m = map(int, input().split())
# lines = [list(map(int, input().split())) for _ in range(m)]
#
# b = [i+1 for i in range(n)]
#
# for l in lines:
#     if l[0] != l[1]:
#         new_b = [b[j] for j in range(l[1]-1,l[0]-2,-1)]
#         j2 = 0
#         for j in range(l[0]-1, l[1]):
#             b[j] = new_b[j2]
#             j2 += 1
#
#
# answer = [str(b[i]) for i in range(n)]
# print(" ".join(answer))

# n = int(input())
# st = str(input())
# an = 0
# for i in range(n):
#     an += int(st[i])
# print(an)
# st = str(input())
# a = [str(-1) for i in range(26)]
# for i in range(len(st), 0, -1):
#     print(st[i-1],ord(st[i-1])-97, str(i-1))
#     a[ord(st[i-1])-97] = str(i-1)
# print(" ".join(a))
# import sys
# data = sys.stdin.readlines()
# for d in data:
#     ar = d.strip().split(" ")
#     an = ""
#     n = int(ar[0])
#     if 1 < len(ar):
#         st = str(ar[1])
#         stl = len(st)
#         for j in range(stl):
#             for i in range(n):
#                 an += st[j]
#         print(an)
# arr = list(map(str, input().strip().split()))
# arr2 = []
# for i in range(2):
#     st = ""
#     for k in range(len(arr[i])):
#         st = arr[i][k]+st
#     arr2.append(int(st))
# print(max(arr2))

# from collections import defaultdict
#
# st = str(input())
# stl = len(st)
# al = defaultdict(int)
# i2 = 2
# i3 = 0
# for i in range(65, 91):
#     al[chr(i)] = i2
#     i3 += 1
#     if i2 != 7 and i2 != 9 and 2 < i3:
#         i2 += 1
#         i3 = 0
#     elif (i2 == 7 or i2 == 9) and 3 < i3:
#         i2 += 1
#         i3 = 0
# an = ""
# for i in range(stl):
#     an += str(al[st[i]])
# print(an)
# st = str(input())
# st_len = len(st)
# mid = st_len // 2
#
# def check(first, end):
#     if first == -1:
#         return 1
#     else:
#         if st[first] == st[end]:
#             return check(first - 1, end + 1)
#         else:
#             return 0
#
# if st_len % 2 == 0:
#     print(check(mid - 1, mid))
# else:
#     print(check(mid - 1, mid + 1))

# from collections import Counter
# st = str(input()).lower()
# arr = [st[i] for i in range(len(st))]
# c = Counter(arr)
# if c.most_common()[0][1] == c.most_common()[1][1]:
#     print("?")
# else:
#     print(c.most_common()[0][0].upper())

# from collections import defaultdict
# level = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
# levelscore = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
# score = defaultdict(float)
# for i in range(9):
#     score[level[i]] = levelscore[i]
# chapter = set()
# allsum = 0
# myallsum = 0
# while True:
#     try:
#         line = input().split(" ")
#         if str(line[2]) != "P":
#             chapter.add(str(line[0]))
#             myallsum += float(line[1])
#             allsum += float(line[1]) * score[str(line[2])]
#     except EOFError:
#         break
#
# print(round(allsum / myallsum, 4))
# import sys
# data = sys.stdin.readlines()
# lines = [list(map(int, line.strip().split())) for line in data]
# n, m = len(lines), len(lines[0])
# max_num = 0
# max_i = 0
# max_j = 0
# for i in range(n):
#     for j in range(m):
#         if max_num < lines[i][j]:
#             max_num = lines[i][j]
#             max_i = i
#             max_j = j
# print(max_num)
# print(max_i+1, max_j+1)

# import sys
# data = sys.stdin.readlines()
# lines = [str(line.strip()) for line in data]
# length = [len(l) for l in lines]
# n, m = len(lines), max(length)
# an = ""
# for j in range(m):
#     for i in range(n):
#         if j < length[i]:
#             an += lines[i][j]
# print(an)
# n = int(input())
# if n == 1 or n == 2:
#     print(n)
# else:
#     start = 2 # A + 6(n-1)
#     i = 1
#     while start < n:
#         start = start+6*(i-1)
#         i += 1
#     if start == n:
#         print(i)
#     else:
#         print(i-1)
# n = int(input())
# route = set()
# i = 1
# sum = 1
# while sum < n:
#     i += 1
#     sum += i
# if i % 2 != 0:
#     x, y = 1, i
#     for _ in range(sum-n):
#         x+=1
#         y-=1
# else:
#     x, y = i, 1
#     for _ in range(sum-n):
#         x-=1
#         y+=1
# print(str(x)+"/"+str(y))

# n = int(input())
# dp = [0] * (n + 1)
# dp[0] = 0
# dp[1] = 1
# dp[2] = 2
# for i in range(3, n + 1):
#     dp[i] = (dp[i - 1] + 1) + (dp[i - 2] + 2)
#
# print(dp[n] % 15746)

# n = 3
# arr = [[26, 40, 83],[49, 60, 57],[13, 89, 99]]
#
# dp  = [[0,1,2] for _ in range(n)]
# dp[0] = [26, 40, 83]
#
# for i in range(1, n):
#     dp[i][0] = arr[i][0] + min(dp[i-1][1],dp[i-1][2])
#     dp[i][1] = arr[i][1] + min(dp[i-1][0],dp[i-1][2])
#     dp[i][2] = arr[i][2] + min(dp[i-1][0],dp[i-1][1])
#
# print(min(dp[n-1]))

# n = 6
# arr = [10,20,15,25,10,20]
#
# dp = [0] * n
# dp[0] = arr[0]
# dp[1] = arr[0]+arr[1]
# dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
# for i in range(3, n):
#     dp[i]=max(dp[i-2],dp[i-3]+arr[i-1])+arr[i]
# print(dp)

# n = 12
# arr = [i for i in range(1,n) if n % i == 0]
# print(arr)
# print(f"{n} = "+" + ".join(str(i) for i in arr))

# n = int(input())
# arr = list(map(int, input().split()))
# max_arr = max(arr)
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
# cal_arr = sieve_of_eratosthenes(max_arr)
# count=0
# for a in arr:
#     if a in cal_arr:
#         count+=1
# print(count)

# n = 6
# wine = [6, 10, 13, 9, 8, 1]
# dp = [0] * n
# dp[0] = wine[0]
# dp[1] = wine[1]+wine[0]
# dp[2] = max(wine[2]+wine[1], wine[1]+wine[0])
# for i in range(4, n):
#     dp[i] = max(dp[i-1],
#                 dp[i-2]+wine[i],
#                 dp[i-3]+wine[i-1]+wine[i])
#
# print(dp[n-1])
#
# min_n = 60
# max_n = 100
#
# num = [i for i in range(max_n+1)]
# num_check = [True] * (max_n+1)
# num_check[0] = False
# num_check[1] = False
# for i in range(2, int(max_n**0.5)):
#     if num_check[i]:
#         for k in range(2*i, max_n, i):
#             num_check[k] = False
#
# num_arr = [i for i in range(max_n) if num_check[i] and min_n <= i]
# print(num_arr)
# print(sum(num_arr))
# print(min(num_arr))
#
# from bisect import bisect_left
#
# def lis(nums):
#     sub = []  # 증가하는 부분 수열을 저장할 배열
#     for x in nums:
#         pos = bisect_left(sub, x)  # x가 들어갈 위치 찾기
#         if pos == len(sub):
#             sub.append(x)  # 새로운 값을 추가
#         else:
#             sub[pos] = x  # 기존 값을 대체
#     return sub
#
# # 예제
# nums = [10, 10, 30, 20, 50]
# print(lis(nums))  # 출력: 4

# def max_satisfaction(budget, items):
#     # 예산과 물품 리스트(items: [(price, satisfaction)])
#     dp = [0] * (budget + 1)
#
#     for price, satisfaction in items:
#         for j in range(budget, price - 1, -1):
#             dp[j] = max(dp[j], dp[j - price] + satisfaction)
#             print(dp)
#     print(budget)
#     return dp
#
# # 예제 입력
# budget = 50
# items = [(20, 60), (30, 90), (10, 50)]  # (price, satisfaction)
#
# # 결과 출력
# print("최대 만족도:", max_satisfaction(budget, items))

# from collections import Counter
# n = 6
# arr = [1,3,8,-2,2,2]
# c = Counter(arr).most_common()
# arr.sort()
# print(int(round(sum(arr)/n,0)))
# print(arr[n//2])
# if 1 < len(c) and c[0][1] == c[1][1]:
#     print(c[1][0])
# else:
#     print(c[0][0])
# print(arr[-1]-arr[0])
# n,m = 10, 13
# board = ["BBBBBBBBWBWBW",
#         "BBBBBBBBBWBWB",
#         "BBBBBBBBWBWBW",
#         "BBBBBBBBBWBWB",
#         "BBBBBBBBWBWBW",
#         "BBBBBBBBBWBWB",
#         "BBBBBBBBWBWBW",
#         "BBBBBBBBBWBWB",
#         "WWWWWWWWWWBWB",
#         "WWWWWWWWWWBWB"]
# board2 = [
#     "BWBWBWBW",
#     "WBWBWBWB",
#     "BWBWBWBW",
#     "WBWBWBWB",
#     "BWBWBWBW",
#     "WBWBWBWB",
#     "BWBWBWBW",
#     "WBWBWBWB",
# ]
# board3 = [
#     "WBWBWBWB",
#     "BWBWBWBW",
#     "WBWBWBWB",
#     "BWBWBWBW",
#     "WBWBWBWB",
#     "BWBWBWBW",
#     "WBWBWBWB",
#     "BWBWBWBW",
# ]
#
# min_count = float('inf')
# for i in range(n-7):
#     for j in range(m-7):
#         count1 = 0
#         count2 = 0
#         for i1 in range(i, i+8):
#             for j1 in range(j, j+8):
#                 if board[i1][j1] != board2[i1-i][j1-j]:
#                     count1 +=1
#                 if board[i1][j1] != board3[i1-i][j1-j]:
#                     count2 +=1
#         min_count = min(min_count, count1, count2)
# print(min_count)

# n = int(input())
# arr = []
# for i in range(n):
#     age, name = map(int, input().split())
#     arr.append([age, i, name])
# arr.sort(key=lambda x: (x[0], x[1]))
#
# for j in range(n):
#     print(arr[j][0], arr[j][2])

# from collections import defaultdict
# n = int(input())
# arr = list(map(int, input().split()))
# mapped_dict = {item: index  for index, item in enumerate(sorted(set(arr)))}
# print(" ".join([str(mapped_dict[i]) for i in arr]))
# a = defaultdict(int)
# a[0]= 10
# print(a.get(1))

import sys
# n,m = 5, 11
# # int(input())
# data = [
# "baekjoononlinejudge",
# "startlink",
# "codeplus",
# "sundaycoding",
# "codingsh",
# "baekjoon",
# "codeplus",
# "codeminus",
# "startlink",
# "starlink",
# "sundaycoding",
# "codingsh",
# "codinghs",
# "sondaycoding",
# "startrink",
# "icerink",
#
# "starlink",
# 10
# ]#sys.stdin.readlines()
#
# from collections import defaultdict
# n = int(input())
# now = defaultdict(int)
# for _ in range(n):
#     name, action = map(str, input().split())
#     if action == "enter":
#         now[name] = 1
#     elif action == "leave":
#         now[name] = 0
# answer = [st for st in now if now[st] == 1]
# answer.sort()
# for st in answer[::-1]:
#     print(st)

# from collections import defaultdict
# import sys
#
# n, m = map(int, input().split())
# #data = sys.stdin.readlines()
# data = [str(input()) for _ in range(n+m)]
# dogam = defaultdict(str)
# for index, st in enumerate(data[:n]):
#     dogam[str(index + 1)] = str(st)
#     dogam[str(st)] = str(index + 1)
#
# for st in data[n:]:
#     print(dogam[str(st)])

# from collections import defaultdict
#
# n = int(input())
# arr = list(map(int, input().strip().split()))
# set_arr = defaultdict(int)
# for a in arr:
#     set_arr[a] += 1
#
# m = int(input())
# arr2 = list(map(int, input().strip().split()))
# answer = []
# for a in arr2:
#     if set_arr.get(a) is not None:
#         answer.append(str(set_arr[a]))
#     else:
#         answer.append(str(0))
# print(" ".join(answer))

# n, m  = map(int, input().split())
# iknow = set(str(input().strip()) for _ in range(n))
# who = set(str(input().strip()) for _ in range(m))
# answer = sorted(w for w in who if w not in iknow)
# count = len(answer)
#
# print(count)
# print("\n".join(answer))

#a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

# st = str(input().strip())
#
# arr = set()
# len_st = len(st)
# for l in range(1, len_st+1):
#     for s in range(len_st-l+1):
#        if st[s:s+l] not in arr:
#             arr.add(st[s:s+l])
# print(len(arr))
# print(arr)
# a, n1 = map(int, input().split())
# b, n2 = map(int, input().split())
# c_num = a*n2 + b*n1
# m_num = n1 * n2
# def gcm(num1, num2):
#     while num2 != 0:
#         num1, num2 = num2, num1%num2
#     return num1
# num = gcm(c_num, m_num)
# print(c_num // num, m_num//num)
#

# import sys
# data = [4, 2, 6, 12, 18]
# n = int(data[0])
# arr = [int(d) for d in data[1:]]
# len_arr = len(arr)
# min_dis = float('inf')
# def gcm(num1, num2):
#     while num2 != 0:
#         num1, num2 = num2, num1%num2
#     return num1
#
# for i in range(len_arr):
#     min_dis = min(min_dis, gcm(min_dis, arr[i]))
# set_arr = set(arr)
# set_arr2 = set(i for i in range(1,max(arr)+1,min_dis))
#
# print( len(set_arr2)- len(set_arr) )

import sys
# n = 3
# arr = [6, 20, 100]
# max_arr = max(arr)
#
# def get_prime_num(n):
#     arr = [i for i in range(n+1)]
#     arr_t = [True] * (n+1)
#     arr_t[0] = False
#     arr_t[1] = False
#     print(arr)
#     for i in range(2, int(n**0.5)+1, 1):
#         for j in range(i*i,n+1,i):
#             arr_t[j] = False
#     answer = [arr[i] for i in range(2, n+1) if arr_t[i]]
#     return answer
#
# prime_num = get_prime_num(max_arr+115)
# for a in arr:
#     for p in prime_num:
#         if a <= p:
#             print(p)
#             break

#import sys
#data = sys.stdin.readlines()
# int(data[0].strip())
# arr = [1, 10,13,100,1000,10000,100000] #list(map(int, data[1:]))
# n = len(arr)
# arr_count = [0] * n
# max_arr = max(arr)
# primelist = get_prime_num((2*max_arr)+10)
#
# for p in primelist:
#     for i in range(n):
#         if arr[i] < p <= 2*arr[i]:
#             arr_count[i] += 1
#
# for c in arr_count:
#     print(c)

# def get_prime_num(n):
#     arr_t = [True] * (n + 1)
#     arr_t[0] = arr_t[1] = False  # 0과 1은 소수가 아님
#     for i in range(2, int(n**0.5) + 1):
#         if arr_t[i]:
#             for j in range(i * i, n + 1, i):
#                 arr_t[j] = False
#     return [i for i in range(2, n + 1) if arr_t[i]]
#
# def count_prime_pairs(prime_list, num):
#     left, right = 0, len(prime_list) - 1
#     count = 0
#     for p in prime_list:
#         if num == p*2:
#             count+=1
#     while left < right:
#         s = prime_list[left] + prime_list[right]
#         if s == num:
#             count += 1
#             left += 1
#             right -= 1
#         elif s < num:
#             left += 1
#         else:
#             right -= 1
#     return count
#
#
# import sys
#
# data = sys.stdin.readlines()
# n = int(data[0].strip())
# arr = list(map(int, data[1:]))
# max_arr = max(arr)
# prime_num = get_prime_num(max_arr)
#
# for a in arr:
#     arr2 = [p for p in prime_num if p < a]
#     print(count_prime_pairs(arr2, a))


# import sys
#
# stack = []
# def com1(x):
#     stack.append(x)
# def com2():
#     if len(stack) == 0:
#         return -1
#     else:
#         return stack.pop()
# def com3():
#     return len(stack)
# def com4():
#     if len(stack) == 0:
#         return 1
#     else:
#         return 0
# def com5():
#     if len(stack) == 0:
#         return -1
#     else:
#         return stack[-1]
#
# data = sys.stdin.readlines()
# orderlist = list(map(str, data[1:]))
# answer = []
# for st in orderlist:
#     order = int(st[0])
#     if order == 1:
#         o, x = st.split(" ")
#         com1(x)
#     elif order == 2:
#         answer.append(str(com2()).strip())
#     elif order == 3:
#         answer.append(str(com3()).strip())
#     elif order == 4:
#         answer.append(str(com4()).strip())
#     elif order == 5:
#         answer.append(str(com5()).strip())
#
# sys.stdout.write("\n".join(answer))

# import sys
# def checker(st):
#     stack = []
#     for char in st:
#         if char == "(" or char == "[":
#             stack.append(char)
#         elif char == ")":
#             if not stack or stack[-1] != "(":
#                 return "no"
#             else:
#                 stack.pop()
#         elif char == "]":
#             if not stack or stack[-1] != "[":
#                 return "no"
#             else:
#                 stack.pop()
#     return "yes" if not stack else "no"
#
# data = sys.stdin.readlines()
# orderlist = list(map(str.strip, data[:-1]))
# answer = [checker(st) for st in orderlist]
# sys.stdout.write("\n".join(answer))

# from collections import deque
# import sys
# data = sys.stdin.readlines()
# n = int(data[0].strip())
# A = list(map(int, data[1].strip().split()))
# B = list(map(int, data[2].strip().split()))
# m = int(data[3].strip())
# quest = list(map(int, data[4].strip().split()))
# C = []
# for i in range(n):
#     if A[i] == 0:
#         C.append(B[i])
# C = deque(C[::-1])
# answer = []
# for q in quest:
#     C.append(q)
#     answer.append(str(C.popleft()))
# print(" ".join(answer))

# 7 4
# apple
# ant
# sand
# apple
# append
# sand
# sand
# from collections import defaultdict
# import sys
# data = sys.stdin.readlines()
# n, k = map(int, data[0].strip().split())
# word_list = defaultdict(list)
# for word in data[1:]:
#     word = str(word.strip())
#     len_word = len(word)
#     if k <= len_word:
#         if word_list.get(word) is not None:
#             word_list[word][0] += 1
#         else:
#             word_list[word] = [1, len_word]
# arr = []
# for w in word_list:
#     arr.append((-word_list[w][0], -word_list[w][1], w))
# arr.sort()
# sys.stdout.write("\n".join([str(a[2]) for a in arr]))

# def recursion(s, l, r ,i):
#     if l >= r: return (1, i)
#     elif s[l] != s[r]: return (0, i)
#     else: return recursion(s, l+1, r-1, i+1)
#
# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1, 1)
#
# n = int(input())
# for _ in range(n):
#     x, y = isPalindrome(str(input().strip()))
#     print(x, y)

# appendnum = []
# def merge_sort(arr, p, r):
#     if p < r:
#         q = (p + r) // 2  # 중간 지점 계산
#         merge_sort(arr, p, q)  # 전반부 정렬
#         merge_sort(arr, q + 1, r)  # 후반부 정렬
#         merge(arr, p, q, r)  # 병합
#
# def merge(arr, p, q, r):
#     # 두 부분 배열 병합
#     tmp = []
#     i, j = p, q + 1
#
#     # 두 부분 배열에서 작은 값을 선택
#     while i <= q and j <= r:
#         if arr[i] <= arr[j]:
#             tmp.append(arr[i])
#             appendnum.append(arr[i])
#             i += 1
#         else:
#             tmp.append(arr[j])
#             appendnum.append(arr[j])
#             j += 1
#
#     # 남은 부분을 처리
#     while i <= q:
#         tmp.append(arr[i])
#         appendnum.append(arr[i])
#         i += 1
#     while j <= r:
#         tmp.append(arr[j])
#         appendnum.append(arr[j])
#         j += 1
#
#     # 정렬된 결과를 원래 배열에 복사
#     for idx, val in enumerate(tmp):
#         arr[p + idx] = val
#
# n,k = map(int, input().split())
# arr = list(map(int, input().split()))
#
# merge_sort(arr, 0 ,n-1)
# print(appendnum)
# print(appendnum[k-1] if k < len(appendnum)  else -1)

"""
1. -가 3N개 있는 문자열에서 시작한다.
2. 문자열을 3등분 한 뒤, 가운데 문자열을 공백으로 바꾼다. 이렇게 하면, 선(문자열) 2개가 남는다.
3. 이제 각 선(문자열)을 3등분 하고, 가운데 문자열을 공백으로 바꾼다. 이 과정은 모든 선의 길이가 1일때 까지 계속 한다.
"""
#
# def kantore(st):
#     l = len(st)
#     # 9 : 0 1 2 3 4 5 6 7 8
#     left = l // 3
#     mid = (l // 3) * 2
#     right  = len(st) -1
#     midst = ""
#     for i in range(left+1, mid+1):
#         midst += " "
#     if left == 1 :
#         return st[:left] + midst + st[mid:]
#     else:
#         return kantore(st[:left]) + midst + kantore(st[mid:])
#
# while True:
#     try:
#         n = int(input())
#         if n < 1:
#             print("-")
#         else:
#             st = "-"*(3**n)
#             print(kantore(st))
#     except EOFError:
#         break

"""
    ***
    * *
    ***
"""
# def draw_star(n):
#     if n == 3:
#         return ["***", "* *", "***"]  # 기본 패턴
#
#     # 크기 n/3의 패턴을 가져옴
#     smaller_pattern = draw_star(n // 3)
#     pattern = []
#
#     # 위쪽 3줄
#     for line in smaller_pattern:
#         pattern.append(line * 3)
#
#     # 가운데 3줄
#     for line in smaller_pattern:
#         pattern.append(line + " " * (n // 3) + line)
#
#     # 아래쪽 3줄
#     for line in smaller_pattern:
#         pattern.append(line * 3)
#
#     return pattern
#
# n = int(input())
# result = draw_star(n)
#
# # 출력
# print("\n".join(result))

# from itertools import product
# n, m = map(int,input().split())
# for c in product(range(1, n + 1), repeat=m):
#     print(" ".join(map(str,c)))

# n,k = map(int, input().split())
#
# def backtrack(start, path):
#     if len(path) == k:
#         print(" ".join(map(str, path)))
#     else:
#         for i in range(start, n+1):
#             path.append(i)
#             backtrack(i, path)
#             path.pop()
#
# backtrack(1, [])

# n = int(input())
# arr = [-1]*n
# answer = []
#
# def use_queen(row):
#     if row == n:
#         answer.append(arr)
#         return
#
#     for col in range(n):
#         if is_safe(row, col):
#             arr[row] = col
#             use_queen(row+1)
#             arr[row] = -1
#
# def is_safe(row, col):
#     for r in range(row):
#         if arr[r] == col or abs(arr[r]-col) == abs(row-r):
#             return False
#     return True
#
# use_queen(0)
# print(len(answer))
from itertools import permutations
# n = int(input())
# arr = list(map(int, input().split()))
# plus, minus, mulit, div = map(int, input().split())
# operator = [0]*plus+[1]*minus+[2]*mulit+[3]*div
# l = len(operator)
# max_num = float("-inf")
# min_num = float("inf")
# def cul(op, a, b):
#     if op == 0:
#         return a+b
#     elif op == 1:
#         return a - b
#     elif op == 2:
#         return a * b
#     elif op == 3:
#         if a < 0:
#             return -(-a//b)
#         else:
#             return a//b
# num = []
# def backtrack(i, k, plus, minus, mulit, div):
#     if i == l:
#         num.append(k)
#         return
#
#     if 0 < plus:
#         backtrack(i+1, cul(0, k, arr[i+1]), plus-1, minus, mulit, div)
#     if 0 < minus:
#         backtrack(i+1, cul(1, k, arr[i+1]), plus, minus-1, mulit, div)
#     if 0 < mulit:
#         backtrack(i+1, cul(2, k, arr[i+1]), plus, minus, mulit-1, div)
#     if 0 < div:
#         backtrack(i+1, cul(3, k, arr[i+1]), plus, minus, mulit, div-1)
#
# backtrack(0, arr[0], plus, minus, mulit, div)
# print(max(num))
# print(min(num))
# def is_valid(arr, row, col, num, row_sets, col_sets, box_sets):
#     # 이미 숫자가 사용된 경우 False
#     if num in row_sets[row] or num in col_sets[col] or num in box_sets[(row // 3, col // 3)]:
#         return False
#     return True
#
# def solve_sudoku(arr, empty_cells, row_sets, col_sets, box_sets, index=0):
#     if index == len(empty_cells):  # 모든 빈 칸을 채운 경우
#         return True
#
#     row, col = empty_cells[index]  # 현재 빈 칸
#     for num in range(1, 10):  # 1부터 9까지 숫자를 시도
#         if is_valid(arr, row, col, num, row_sets, col_sets, box_sets):
#             # 숫자 배치
#             arr[row][col] = num
#             row_sets[row].add(num)
#             col_sets[col].add(num)
#             box_sets[(row // 3, col // 3)].add(num)
#
#             # 다음 빈 칸으로 진행
#             if solve_sudoku(arr, empty_cells, row_sets, col_sets, box_sets, index + 1):
#                 return True
#
#             # 실패 시 되돌리기
#             arr[row][col] = 0
#             row_sets[row].remove(num)
#             col_sets[col].remove(num)
#             box_sets[(row // 3, col // 3)].remove(num)
#
#     return False  # 가능한 숫자가 없으면 실패
#
# # 입력 및 초기화
# arr = [list(map(int, input().split())) for _ in range(9)]
#
# empty_cells = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]
#
# row_sets = [set(row) for row in arr]
# col_sets = [set(arr[i][j] for i in range(9)) for j in range(9)]
# box_sets = {(i, j): set(arr[x][y] for x in range(i * 3, i * 3 + 3) for y in range(j * 3, j * 3 + 3))
#             for i in range(3) for j in range(3)}
#
# # 스도쿠 풀이
# if solve_sudoku(arr, empty_cells, row_sets, col_sets, box_sets):
#     for row in arr:
#         print(" ".join(map(str, row)))
# else:
#     print("No solution exists")

# import sys
# data = sys.stdin.readlines()
# n, k = map(int, data[0].split())
# arr = [[0]*(n+1)] + [[0]+list(map(int, d.split())) for d in data[1:n+1]]
# S = arr[:]
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         S[i][j] += S[i-1][j]
#         S[i][j] += S[i][j-1]
#         S[i][j] -= S[i-1][j-1]
# for d in data[n+1:]:
#     x1,y1,x2,y2 = map(int, d.split())
#     result = S[x2][y2]
#     result -= S[x1-1][y2]
#     result -= S[x2][y1-1]
#     result += S[x1-1][y1-1]
#     print(result)

# n, k  = map(int, input().split())
# arr = list(map(int, input().split()))
# for i in range(1, n):
#     arr[i] = arr[i] + arr[i-1]
#
# maxnum = arr[k-1]
# for i in range(k, n):
#     maxnum = max(maxnum, arr[i]-arr[i-k])
#
# print(maxnum)

# import sys
# from collections import defaultdict
#
# data = sys.stdin.readlines()
# st = list(data[0].strip())
# k = int(data[1])
# queries = data[2:]
# al_list = defaultdict(int)
# st_arr = [defaultdict(int)]
#
# for char in st:
#     current = st_arr[-1].copy()
#     current[char] += 1
#     st_arr.append(current)
#
# for query in queries:
#     alpha, start, end = query.split()
#     start, end = int(start), int(end)
#     if start == 0:
#         print(st_arr[end + 1][alpha])
#     else:
#         print(st_arr[end + 1][alpha] - st_arr[start][alpha])

# 5 3
# 1 2 3 1 2
# 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수

# import sys
# from collections import defaultdict
# data = sys.stdin.readlines()
# n, k  = map(int, data[0].split())
# arr = list(map(int, data[1].split()))
# prefix_sum = 0
# remainder_count = defaultdict(int)
# remainder_count[0] = 1
#
# count = 0
# for num in arr:
#     prefix_sum += num
#     remainder = prefix_sum % k
#
#     if remainder < 0:
#         remainder += k
#
#     count += remainder_count[remainder]
#     remainder_count[remainder] += 1
#
# print(count)
#
#import sys
# data = sys.stdin.readlines()
# n, m, k = map(int, data[0].split())
# board = [str(d) for d in data[1:]]
#
# switch_zeroone_w = [[0] * (m+1) for _ in range(n+1)]
# switch_zeroone_b = [[0] * (m+1) for _ in range(n+1)]
#
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         need_block_1 = (i+j) % 2
#         need_block_2 = (i+j+1) % 2
#         current_block = 1 if board[i-1][j-1] == "B" else 0
#         switch_zeroone_w[i][j] = need_block_1 ^ current_block
#         switch_zeroone_b[i][j] = need_block_2 ^ current_block
#
#         switch_zeroone_w[i][j] += switch_zeroone_w[i-1][j]+switch_zeroone_w[i][j-1]-switch_zeroone_w[i-1][j-1]
#         switch_zeroone_b[i][j] += switch_zeroone_b[i-1][j]+switch_zeroone_b[i][j-1]-switch_zeroone_b[i-1][j-1]
#
# min_change = float('inf')
# for i in range(k, n+1):
#     for j in range(k, m+1):
#         change_w = switch_zeroone_w[i][j]-switch_zeroone_w[i-k][j]-switch_zeroone_w[i][j-k]+switch_zeroone_w[i-k][j-k]
#         change_b = switch_zeroone_b[i][j]-switch_zeroone_b[i-k][j]-switch_zeroone_b[i][j-k]+switch_zeroone_b[i-k][j-k]
#         min_change = min(min_change, change_w, change_b)
#
# print(min_change)

#5
#3 1 4 3 2\
# expression = input()
# groups = expression.split('-')
# result = sum(map(int, groups[0].split('+')))
# for group in groups[1:]:
#     result -= sum(map(int, group.split('+')))
# print(result)

# st = str(input())
# st_minus = st.split("-")
# sumplus = [sum(map(int, minus.split("+"))) for minus in st_minus]
# print(sumplus[0]-sum(sumplus[1:]))

# 4
# 2 3 1
# 5 2 4 1
# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14
# import sys
# data = sys.stdin.readlines()
# st = int(data[0])
# arr = [list(map(int, d.strip().split())) for d in data[1:]]
# arr.sort(key=lambda x: (x[1], x[0]))
#
# end_time = 0
# count = 0
# for start, end in arr:
#     if end_time <= start:
#         end_time = end
#         count += 1
#
# print(count)

"""
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
"""

# import sys
# data = sys.stdin.readlines()
# n = int(data[0].strip())
# paper = [list(map(int, d.split())) for d in data[1:]]
#
# white_paper = 0
# blue_paper = 0
#
# def paper_checker(x, y, size):
#     global white_paper, blue_paper
#
#     color = paper[x][y]
#     for i in range(size):
#         for j in range(size):
#             if color != paper[x+i][y+j]:
#                 next_size = size // 2
#                 paper_checker(x, y, next_size)
#                 paper_checker(x+next_size, y, next_size)
#                 paper_checker(x, y+next_size, next_size)
#                 paper_checker(x+next_size, y+next_size, next_size)
#                 return
#     if color == 0:
#         white_paper += 1
#     else:
#         blue_paper += 1
#
# paper_checker(0, 0, n)
# print(white_paper)
# print(blue_paper)
"""
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
"""
# import sys
# data = sys.stdin.readlines()
# n = int(data[0].strip())
# makezip = [[int(t) for t in d.strip()] for d in data[1:]]
# text = ""
# def playzip(x, y, size):
#     global text
#     #text+="("
#     num = makezip[x][y]
#     next_size = size // 3
#     for i in range(size):
#          for j in range(size):
#             if num != makezip[x + i][y + j]:
#                 text += "("
#                 playzip(x, y, next_size)
#                 playzip(x, y + next_size, next_size)
#                 playzip(x + next_size, y, next_size)
#                 playzip(x + next_size, y + next_size, next_size)
#                 text += ")"
#                 return
#     if num == 1:
#         text += "1"
#     else:
#         text += "0"
# playzip(0, 0, n)
# print(text)
# ((110(0101))(0010)1(0001))
# 1100101001010001
"""
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
"""
# import sys
# data = sys.stdin.readlines()
# n = int(data[0].strip())
# paper = [list(map(int,d.strip().split())) for d in data[1:]]
# one = 0
# zero = 0
# minus_one = 0
# def divide(x, y, size):
#     global one, zero, minus_one
#
#     color = paper[x][y]
#     for i in range(size):
#         for j in range(size):
#             if paper[x+i][y+j] != color:
#                 next_size = size // 3
#                 divide(x, y, next_size)
#                 divide(x+next_size, y, next_size)
#                 divide(x+next_size+next_size, y, next_size)
#                 divide(x+next_size+next_size, y+next_size, next_size)
#                 divide(x+next_size, y+next_size, next_size)
#                 divide(x, y+next_size, next_size)
#                 divide(x, y+next_size+next_size, next_size)
#                 divide(x+next_size, y+next_size+next_size, next_size)
#                 divide(x+next_size+next_size, y+next_size+next_size, next_size)
#                 return
#     if color == 0:
#         zero+=1
#     elif color == 1:
#         one+=1
#     else:
#         minus_one+=1
# divide(0, 0, n)
# print(minus_one)
# print(zero)
# print(one)

# 10 11 12 -> 4
# n, k, d = map(int, input().split())
# def sqrt(n, k):
#     if k == 0:
#         return 1
#     elif k % 2 == 0:
#         half = sqrt(n, k // 2)
#         return (half * half) % d
#     else:
#         half = sqrt(n, (k - 1) // 2)
#         return (n * half * half) % d
# print(sqrt(n, k)%d)


# 5 2
# 이항계수  = n!/k!*(n-k)!
# mod = 1_000_000_007
# n, k = map(int, input().split())
#
# def mod_factorial(n):
#     fact = [1]*(n+1)
#     for i in range(2, n+1):
#         fact[i] = fact[i-1]*i % mod
#     return fact
#
# def mod_inverse(a):
#     return pow(a, mod - 2, mod)
#
# def binomial_coefficient(n, k):
#     if k > n:
#         return 0
#     fact = mod_factorial(n)
#     numerator = fact[n]
#     denominator = (fact[k] * fact[n - k]) % mod
#     return numerator * mod_inverse(denominator) % mod
#
# print(binomial_coefficient(n, k))
"""
2 5
1 2
3 4
"""
# import sys
# data = sys.stdin.readlines()
# n, k = map(int, data[0].split())
# A = [list(map(int,d.split())) for d in data[1:]]
# mod = 1000
#
# def matrix_sqrt(A, B):
#     C = [[0]*n for _ in range(n)]
#
#     for i in range(n):  # 행렬 A의 행 인덱스
#         for j in range(n):  # 행렬 B의 열 인덱스
#             for l in range(n):  # A의 열 인덱스와 B의 행 인덱스
#                 C[i][j] += A[i][l] * B[l][j]
#                 C[i][j] %= mod
#     return C
#
# def conq(A, k):
#     if k == 1:
#         return A
#     if k % 2 == 0:
#         B = conq(A, k//2)
#         return matrix_sqrt(B, B)
#     elif k % 2 == 1:
#         B = conq(A, k-1)
#         return matrix_sqrt(A, B)
#
# C = conq(A, k)
# for row in C:
#     print(" ".join(map(str, row)))

# n = int(input())
# mod = 1_000_000_007
#
# def matrix_sqrt(A, B):
#     C = [[0,0],[0,0]]
#
#     for i in range(2):  # 행렬 A의 행 인덱스
#         for j in range(2):  # 행렬 B의 열 인덱스
#             for l in range(2):  # A의 열 인덱스와 B의 행 인덱스
#                 C[i][j] += A[i][l] * B[l][j]
#                 C[i][j] %= mod
#     return C
#
# def conq(A, k):
#     if k == 1:
#         return A
#     if k % 2 == 0:
#         B = conq(A, k//2)
#         return matrix_sqrt(B, B)
#     elif k % 2 == 1:
#         B = conq(A, k-1)
#         return matrix_sqrt(A, B)
#
# A = [[1,1],[1,0]]
# C = conq(A, n)
#
# print(C[0][1])

#
# import sys, heapq
# data = sys.stdin.readlines()
#
# q = []
# results = []
#
# for d in data[1:]:
#     d = int(d)
#     if d < 0:
#         heapq.heappush(q, (abs(d), -1))
#     elif 0 < d:
#         heapq.heappush(q, (d, 1))
#     else:
#         if 0 < len(q):
#             x, y = heapq.heappop(q)
#             results.append(x*y)
#         else:
#             results.append(0)
#
# sys.stdout.write("\n".join(map(str, results)) + "\n")

# import sys
# data = sys.stdin.readlines()
# n, k = map(int, data[0].split())
# arr = [int(d) for d in data[1:]]
# # 1,  1,000,000
# min_cm = 1
# max_cm = max(arr)
# answer = 0
# while min_cm < max_cm:
#     half = (min_cm+max_cm) // 2
#     count = 0
#     for a in arr:
#         count += a // half
#
#     if count == k:
#         answer = min_cm
#         min_cm += 1
#     elif count < k:
#         max_cm = half
#     elif count > k:
#         min_cm = half
#
# print(answer)


# import sys
# data = sys.stdin.readlines()
# n, k = map(int, data[0].split())
# arr = list(map(int, data[1].split()))
#
# left = 1
# right = max(arr)
# answer = 0
# while left <= right:
#     half = (left+right) // 2
#     count = sum([a-half for a in arr if 0 < a-half])
#     print(left,right)
#     if count >= k:
#         answer = half
#         left = half+1
#     elif count < k:
#         right = half-1
#
# print(answer)

# """
# 6
# 10 20 10 30 20 50
# """
# from bisect import bisect_left
# import sys
# data = sys.stdin.readlines()
# n = int(data[0])
# arr = list(map(int, data[1].split()))
# mini = []
# len_count = 0
# for a in arr:
#     check = bisect_left(mini,a)
#     if check == len_count:
#         mini.append(a)
#         len_count += 1
#     else:
#         mini[check] = a
#
# print(len_count)

# from collections import defaultdict
# import sys
# sys.setrecursionlimit(100000)
#
# order = 1
# def dfs(node, graph, visit_order):
#     global order
#     visit_order[node] = order
#     order+=1
#     for neighbor in graph[node]:
#         if visit_order[neighbor] == 0:  # 아직 방문하지 않은 경우
#             dfs(neighbor, graph, visit_order)
#
# # 입력 처리
# input = sys.stdin.read
# data = input().splitlines()
#
# n, m, r = map(int, data[0].split())  # 정점 수, 간선 수, 시작 정점
# graph = defaultdict(list)
#
# # 그래프 구성
# for line in data[1:]:
#     u, v = map(int, line.split())
#     graph[u].append(v)
#     graph[v].append(u)
#
# # 인접 정점 정렬
# for node in graph:
#     graph[node].sort()
#
# # 방문 순서 저장 배열
# visit_order = [0] * (n + 1)
# # DFS 탐색 시작
# dfs(r, graph, visit_order)
#
# # 결과 출력
# print("\n".join(map(str, visit_order[1:])))

# from collections import defaultdict, deque
#
# def dfs(graph, start, visited, result):
#     visited[start] = True
#     result.append(start)  # 방문 순서 기록
#
#     for neighbor in graph[start]:
#         if not visited[neighbor]:
#             dfs(graph, neighbor, visited, result)
#
# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     result = []
#
#     while queue:
#         node = queue.popleft()
#         result.append(node)  # 방문 순서 기록
#
#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 queue.append(neighbor)
#
#     return result
#
# # 입력 처리
# n, m, v = map(int, input().split())  # 정점 수, 간선 수, 시작 정점 번호
# graph = defaultdict(list)
#
# for _ in range(m):
#     u, w = map(int, input().split())
#     graph[u].append(w)
#     graph[w].append(u)
#
# # 인접 정점 오름차순 정렬
# for node in graph:
#     graph[node].sort()
#
# # DFS 탐색
# visited_dfs = [False] * (n + 1)
# dfs_result = []
# dfs(graph, v, visited_dfs, dfs_result)
#
# # BFS 탐색
# visited_bfs = [False] * (n + 1)
# bfs_result = bfs(graph, v, visited_bfs)
#
# # 출력
# print(" ".join(map(str, dfs_result)))
# print(" ".join(map(str, bfs_result)))
#
# from collections import deque
#
# def bfs_shortest_time(n, k):
#     # 방문 배열 (최대 위치 100,000)
#     max_pos = 100000
#     visited = [False] * (max_pos + 1)
#
#     # BFS 큐 초기화 (위치, 시간)
#     queue = deque([(n, 0)])
#     visited[n] = True
#
#     while queue:
#         position, time = queue.popleft()
#
#         # 동생 위치에 도달한 경우
#         if position == k:
#             return time
#
#         # 가능한 이동
#         for next_pos in (position - 1, position + 1, position * 2):
#             if 0 <= next_pos <= max_pos and not visited[next_pos]:
#                 visited[next_pos] = True
#                 queue.append((next_pos, time + 1))
#
# # 입력
# n, k = map(int, input().split())
#
# # 결과 출력
# print(bfs_shortest_time(n, k))

# from collections import deque
#
# def bfs(start, end, visited, field, n):
#     directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]  # 이동방식
#     queue = deque([])
#     (sx, sy) = start
#     queue.append(((sx, sy), 0))
#     visited[sx][sy] = True
#
#     while queue:
#         (cx, cy), distance = queue.popleft()
#         if (cx, cy) == end:
#             return distance
#         for dx, dy in directions:
#             nx, ny = cx + dx, cy + dy
#             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 queue.append(((nx, ny), distance + 1))
#
# def solve():
#     t = int(input())
#     for _ in range(t):
#         n = int(input().strip())  # 배추밭 크기(MxN)와 배추 개수(K)
#         field = [[0] * n for _ in range(n)]
#         visited = [[False] * n for _ in range(n)]
#
#         (sx, sy) = map(int, input().split())
#         (ex, ey) = map(int, input().split())
#         print(bfs((sx, sy), (ex, ey), visited, field, n))
#
# solve()
"""
mirkovC4nizCC44
C4
'FRULA'
"""
# st = str(input())
# boom = str(input())
# len_boom = len(boom)
# checker = []
# for s in st:
#     checker.append(s)
#     if "".join(checker[-len_boom:]) == boom:
#         del checker[-len_boom:]
# if checker:
#     print("".join(checker))
# else:
#     print('FRULA')

# from collections import deque
# import sys
#
# def bfs(start, end, visited, board, n, m):
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 이동방식
#     queue = deque([(start[0], start[1], 1, False)])  # (x, y, 거리, 벽 부순 여부)
#     visited[start[0]][start[1]][0] = True
#
#     while queue:
#         x, y, dist, wall_broken = queue.popleft()
#
#         # 종료 조건: 도착 지점에 도달
#         if (x, y) == end:
#             return dist
#
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#
#             if 0 <= nx < n and 0 <= ny < m:  # 유효한 좌표
#                 if board[nx][ny] == 0:  # 벽이 없는 경우
#                     if not visited[nx][ny][wall_broken]:
#                         visited[nx][ny][wall_broken] = True
#                         queue.append((nx, ny, dist + 1, wall_broken))
#                 elif board[nx][ny] == 1 and not wall_broken:  # 벽이 있고 아직 벽을 부수지 않은 경우
#                     if not visited[nx][ny][1]:  # 벽을 부순 상태로 방문하지 않은 경우
#                         visited[nx][ny][1] = True
#                         queue.append((nx, ny, dist + 1, True))
#
#     return -1  # 도달할 수 없는 경우
#
# # 입력 처리
# data = sys.stdin.readlines()
# n, m = map(int, data[0].split())
# board = [list(map(int, data[i + 1].strip())) for i in range(n)]
#
# # 방문 배열 초기화
# visited = [[[False, False] for _ in range(m)] for _ in range(n)]
#
# # 결과 출력
# print(bfs((0, 0), (n - 1, m - 1), visited, board, n, m))
# from collections import deque, defaultdict
#
#
# def bfs(edge, n):
#     visited = [0] * (n + 1)  # 방문 배열: 0은 미방문, 1과 2는 두 가지 색
#     for node in range(1, n + 1):  # 모든 정점을 확인 (연결되지 않은 경우 대비)
#         if visited[node] == 0:  # 아직 방문하지 않은 정점이면 BFS 시작
#             queue = deque([node])
#             visited[node] = 1  # 시작점은 1번 색으로 지정
#
#             while queue:
#                 node = queue.popleft()
#                 current_color = visited[node]
#                 next_color = 2 if current_color == 1 else 1
#
#                 for neighbor in edge[node]:
#                     if visited[neighbor] == 0:  # 아직 방문하지 않은 경우
#                         visited[neighbor] = next_color
#                         queue.append(neighbor)
#                     elif visited[neighbor] == current_color:  # 색이 같으면 이분 그래프 아님
#                         return "NO"
#     return "YES"
#
# import sys
# data = sys.stdin.readlines()
# # 입력 처리
# t = int(data[0].strip())  # 테스트 케이스 개수
# index = 1
# results = []
# for _ in range(t):
#     n, c = map(int, data[index].strip().split())  # 정점과 간선 개수
#     index += 1
#     edge = defaultdict(list)
#     for _ in range(c):
#         a, b = map(int, data[index].strip().split())
#         index += 1
#         edge[a].append(b)
#         edge[b].append(a)
#     results.append(bfs(edge, n))
#
# sys.stdout.write("\n".join(results) + "\n")

#Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수
# n = int(input())
# arr = list(map(int, input().split()))
# result = [-1] * n
# stack = []
#
# for i in range(n - 1, -1, -1):
#     while stack and arr[stack[-1]] <= arr[i]:
#         stack.pop()
#     if stack:
#         result[i] = arr[stack[-1]]
#     stack.append(i)
#
# print(" ".join(str(i) for i in result))

#Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수
# from collections import Counter
# n = int(input())
# arr = list(map(int, input().split()))
# result = [-1] * n
# count = Counter(arr)
# stack = []
# for i in range(n - 1, -1, -1):
#     while stack and count[arr[stack[-1]]] <= count[arr[i]]:
#         stack.pop()
#     if stack:
#         result[i] = arr[stack[-1]]
#     stack.append(i)
#
# print(" ".join(str(i) for i in result))

# n,k = map(int, input().split())
# coins = [int(input()) for _ in range(n)]
#
# dp = [0]* (k+1)
# dp[0] = 1
#
# for coin in coins:
#     for i in range(coin, k+1):
#         dp[i] = dp[i] + dp[i-coin]
#
# print(dp[k])

# n = int(input())
# weights = list(map(int, input().split()))
# q = int(input())
# target = list(map(int, input().split()))
#
# possible = {0}
# for w in weights:
#     set_newpossible = set()
#     for p in possible:
#         set_newpossible.add(p+w)
#         set_newpossible.add(abs(p-w))
#     possible.update(set_newpossible)
#
# result = []
# for t in target:
#     if t in possible:
#         result.append("Y")
#     else:
#         result.append("N")
# print(" ".join(result))

# def getMaxArea(heights, left, right):
#     if right == left:
#         return heights[left]
#
#     mid = (right+left) // 2
#     leftArea = getMaxArea(heights, left, mid)
#     rightArea = getMaxArea(heights, mid+1,right)
#     middle_area = getMiddleArea(heights, left, mid, right)
#
#     # 가장 큰 값 반환
#     return max(leftArea, rightArea, middle_area)
#
# def getMiddleArea(heights, left, mid, right):
#     l = mid
#     r = mid+1
#     height = min(heights[l],heights[r])
#     max_area = 2 * height
#     while left < l or r < right:
#         if r < right and (l == left or heights[r+1] > heights[l-1]):
#             r+=1
#             height = min(height, heights[r])
#         else:
#             l-=1
#             height = min(height, heights[l])
#         max_area = max(max_area, height * (r - l + 1))
#
#     return max_area
#
# import sys
# data = sys.stdin.readlines()
# for d in data[:-1]:
#     heights = list(map(int, d.split()))
#     print(getMaxArea(heights[1:], 0, len(heights[1:]) - 1))
#
# def largestRectangleArea(heights):
#     stack = []
#     max_area = 0
#     index = 0
#
#     while index < len(heights):
#         if not stack or heights[index] >= heights[stack[-1]]:
#             stack.append(index)
#             index += 1
#         else:
#             top_of_stack = stack.pop()
#             height = heights[top_of_stack]
#             width = index if not stack else index - stack[-1] -1
#             max_area = max(max_area, height*width)
#
#     while stack:
#         top_of_stack = stack.pop()
#         height = heights[top_of_stack]
#         width = index if not stack else index - stack[-1] -1
#         max_area = max(max_area, height*width)
#
#     return max_area
#
# import sys
# data = sys.stdin.readlines()
# print(largestRectangleArea(data[1:]))

# def count_visible_pairs(heights):
#     stack = []  # 스택 초기화
#     pair_count = 0  # 쌍의 수를 저장할 변수
#
#     for height in heights:
#         # 현재 사람보다 작은 키의 사람을 스택에서 제거하며 쌍 계산
#         same_height_count = 1
#         while stack and stack[-1][0] <= height:
#             top_height, count = stack.pop()
#             pair_count += count  # 쌍 추가
#             if top_height == height:
#                 same_height_count += count  # 동일한 키 처리
#
#         # 현재 사람을 스택에 추가
#         if stack:
#             pair_count += 1  # 스택에 남아 있는 사람과 현재 사람은 서로 볼 수 있음
#         stack.append((height, same_height_count))
#
#     return pair_count
#
# # 입력 처리
# import sys
# input = sys.stdin.read
# data = input().split()
# N = int(data[0])
# heights = list(map(int, data[1:]))
#
# # 결과 출력
# result = count_visible_pairs(heights)
# print(result)

"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""

# n, e = map(int, input().strip().split())
# start = int(input().strip())
#
# dp = [[float('inf')]*(n+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     dp[i][i] = 0
#
# for _ in range(e):
#     u, v, w = map(int, input().strip().split())
#     dp[u][v] = min(dp[u][v], w)
#
# for leng in range(2, n+1):
#     for i in range(1, n+1-leng):
#         j = i+leng
#         for k in range(i, j):
#             dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
#
# for i in range(1, n+1):
#     print(dp[1][i])

# """
# N과 간선의 개수 E
# 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c
# 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2
# """
# from collections import defaultdict
# import heapq, sys
#
# data = sys.stdin.readlines()
# node_c, edge_c = map(int, data[0].strip().split())
# graph = defaultdict(list)
# for d in data[1:-1]:
#     a, b, c = map(int, d.strip().split())
#     graph[a].append((c, b))
#     graph[b].append((c, a))
#
# v1,v2 = map(int, data[-1].strip().split())
#
# def dijkstra(start, graph, n):
#     distance  = [float('inf')]*(n+1)
#     distance[start] = 0
#     q = []
#     heapq.heappush(q, (0, start))
#     while q:
#         dist, node = heapq.heappop(q)
#         if dist > distance[node]:
#             continue
#         for need_dist, ne in graph[node]:
#             next_dist = need_dist+dist
#             if next_dist < distance[ne]:
#                 distance[ne] = next_dist
#                 heapq.heappush(q,(next_dist, ne))
#
#     return distance
#
# one_dist = dijkstra(1, graph, node_c)
# v1_dist = dijkstra(v1, graph, node_c)
# v2_dist = dijkstra(v2, graph, node_c)
# answer = min(one_dist[v1]+v1_dist[v2]+v2_dist[0],one_dist[v2]+v2_dist[v1]+v1_dist[0])
# print(answer if answer != float('inf') else -1)
"""
첫 번째 줄에는 테스트 케이스의 T(1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스마다
첫 번째 줄에 3개의 정수 n, m, t (2 ≤ n ≤ 2 000, 1 ≤ m ≤ 50 000 and 1 ≤ t ≤ 100)가 주어진다. 각각 교차로, 도로, 목적지 후보의 개수이다.
두 번째 줄에 3개의 정수 s, g, h (1 ≤ s, g, h ≤ n)가 주어진다. s는 예술가들의 출발지이고, g, h는 문제 설명에 나와 있다. (g ≠ h)
그 다음 m개의 각 줄마다 3개의 정수 a, b, d (1 ≤ a < b ≤ n and 1 ≤ d ≤ 1 000)가 주어진다. a와 b 사이에 길이 d의 양방향 도로가 있다는 뜻이다.
그 다음 t개의 각 줄마다 정수 x가 주어지는데, t개의 목적지 후보들을 의미한다. 이 t개의 지점들은 서로 다른 위치이며 모두 s와 같지 않다.
"""
# from heapq import heappop, heappush
# from collections import defaultdict
# import sys
#
# input = sys.stdin.read
# def dijkstra(start, graph, n):
#     distances = [float('inf')] * (n + 1)
#     distances[start] = 0
#     q = []
#     heappush(q, (0, start))
#
#     while q:
#         current_dist, current_node = heappop(q)
#         if current_dist > distances[current_node]:
#             continue
#
#         for next_dist, next_node in graph[current_node]:
#             new_dist = current_dist + next_dist
#             if new_dist < distances[next_node]:
#                 distances[next_node] = new_dist
#                 heappush(q, (new_dist, next_node))
#
#     return distances
#
#
# def solve():
#     data = input().splitlines()
#     T = int(data[0])
#     idx = 1
#
#     results = []
#     for _ in range(T):
#         # 입력 처리
#         n, m, t = map(int, data[idx].split())
#         idx += 1
#         s, g, h = map(int, data[idx].split())
#         idx += 1
#
#         graph = defaultdict(list)
#         for __ in range(m):
#             a, b, d = map(int, data[idx].split())
#             graph[a].append((d, b))
#             graph[b].append((d, a))
#             idx += 1
#
#         candidates = []
#         for __ in range(t):
#             candidates.append(int(data[idx]))
#             idx += 1
#
#         # 다익스트라 실행
#         dist_from_s = dijkstra(s, graph, n)
#         dist_from_g = dijkstra(g, graph, n)
#         dist_from_h = dijkstra(h, graph, n)
#
#         # 후보 확인
#         valid_destinations = []
#         for dest in candidates:
#             # 두 경로 중 하나라도 최단 경로라면 유효
#             through_g_h = dist_from_s[g] + dist_from_g[h] + dist_from_h[dest]
#             through_h_g = dist_from_s[h] + dist_from_h[g] + dist_from_g[dest]
#
#             if dist_from_s[dest] != float('inf') and (dist_from_s[dest] == through_g_h or dist_from_s[dest] == through_h_g):
#                 valid_destinations.append(dest)
#
#         # 결과 저장
#         results.append(" ".join(map(str, sorted(valid_destinations))))
#
#     # 결과 출력
#     sys.stdout.write("\n".join(results) + "\n")
# solve()

"""
3 4
1 2 4
1 3 3
2 3 -1
3 1 -2
"""
#
# def bellman_ford(start, graph, V):
#     distance = [float('inf')] * (V+1)
#     distance[start] = 0
#
#     for _ in range(V - 1): #
#         for u, v, weight in graph:
#             if distance[u] + weight < distance[v]:
#                 distance[v] = distance[u] + weight
#
#     for u, v, weight in graph:
#         if distance[u] + weight < distance[v]:
#             return -1
#     return_dist = [-1 if x == float('inf') else x for x in distance[2:]]
#     return return_dist
#
# import sys
# data = sys.stdin.readlines()
# V, e = map(int, data[0].strip().split())
# graph = []
# for d in data[1:]:
#     u, v, weight = map(int, d.strip().split())
#     graph.append((u, v, weight))
#
# result = bellman_ford(1, graph, V)
# sys.stdout.write("\n".join(str(r) for r in result) if result != -1 else "-1")

# import sys
# input = sys.stdin.readline
#
# # 입력 처리
# n = int(input())  # 도시 개수
# m = int(input())  # 버스 개수
#
# INF = float('inf')
# dist = [[INF] * (n + 1) for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     dist[i][i] = 0
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     dist[a][b] = min(dist[a][b], c)
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if dist[i][j] == INF:
#             print(0, end=" ")
#         else:
#             print(dist[i][j], end=" ")
#     print()
"""
3 4
1 2 1
3 2 1
1 3 5
2 3 2
"""

# def floyd_warshall(graph, n):
#     dist = [[float('inf')] * (n+1) for _ in range((n+1))]
#
#     for a,b,c in graph:
#         dist[a][b] = min(dist[a][b], c)
#
#     for k in range(1, n + 1):
#         for i in range(1, n + 1):
#             for j in range(1, n + 1):
#                 dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
#     result = [dist[i][i] for i in range(1, n + 1) if dist[i][i] != float('inf')]
#     return result
#
# import sys
# data = sys.stdin.readlines()
# n, e = map(int, data[0].strip().split())
# graph = []
# for d in data[1:]:
#     a,b,c = map(int, d.strip().split())
#     graph.append((a,b,c))
#
# result = floyd_warshall(graph, n)
# print(min(result) if 0 < len(result) else -1)

# n = int(input())
# arr = list(map(int, input().strip().split()))
# sum_num = int(input())
#
# arr.sort()
# left, right = 0, n - 1
# count = 0
#
# while left < right:
#     c_sum = arr[left]+arr[right]
#     if sum_num == c_sum:
#         count += 1
#         left += 1
#         right -= 1
#     elif sum_num < c_sum:
#         right -= 1
#     else:
#         left += 1
#
# print(count)

# n = int(input())
# arr = list(map(int, input().strip().split()))
# arr.sort()
#
# left, right = 0, n - 1
# min_gap = float('inf')
# answer_left, answer_right = 0, 0
# while left < right:
#     gap = arr[left]+arr[right]
#     if abs(gap) < min_gap:
#         min_gap = abs(gap)
#         answer_left, answer_right = arr[left], arr[right]
#
#     # 포인터 이동
#     if gap < 0:  # 혼합 값이 음수면 더 큰 값을 만들기 위해 left 증가
#         left += 1
#     elif gap > 0:  # 혼합 값이 양수면 더 작은 값을 만들기 위해 right 감소
#         right -= 1
#     else:  # 혼합 값이 0이면 최적의 결과
#         break
# print(answer_left, answer_right)


"""
10 15
5 1 3 5 10 7 4 9 2 8
s 이상 값 중 거리가 제일 가까운 것 
9 10
3 1 1 1 2 2 2 2 2
"""
# n, s = map(int, input().strip().split())
# arr = list(map(int, input().strip().split()))
#
# # 슬라이딩 윈도우 초기화
# start = 0
# current_sum = 0
# min_length = float('inf')
#
# for end in range(n):
#     current_sum += arr[end]
#     while current_sum >= s:
#         min_length = min(min_length, end - start + 1)
#         current_sum -= arr[start]
#         start += 1
#
# # 결과 출력
# print(min_length if min_length != float('inf') else 0)

# n = int(input())
# numbers = [True] * (n+1)
# numbers[0] = False
# numbers[1] = False
# for i in range(2, int(n**0.5)+1):
#     if numbers[i]:
#         for j in range(i*i, n+1, i):
#             numbers[j] = False
#
# prime_num = [i for i in range(n+1) if numbers[i]]
# l = len(prime_num)
#
# current_sum = 0
# start = 0
# count = 0
# for end in range(l):
#     current_sum += prime_num[end]
#     if current_sum == n:
#         count += 1
#     while n <= current_sum:
#         current_sum -= prime_num[start]
#         if current_sum == n:
#             count += 1
#         start += 1
#
# print(count)

# from itertools import combinations
# import sys
# data = sys.stdin.readlines()
# n ,c = map(int, data[0].strip().split())
# arr = list(map(int, data[1].strip().split()))
#
# def all_comb_sum(ar):
#     comb_sums = []
#     for i in range(len(ar)+1):
#         for p in combinations(ar, i):
#             comb_sums.append(sum(p))
#     return comb_sums
#
# left_sums = all_comb_sum(arr[:n//2])
# right_sums = all_comb_sum(arr[n//2:])
# right_sums.sort()
#
# count = 0
# for left_sum in left_sums:
#     if left_sum <= c:
#         low, high = 0, len(right_sums)
#         while low < high:
#             mid = (low + high) // 2
#             if left_sum+right_sums[mid] <= c:
#                 low = mid + 1
#             else:
#                 high = mid
#         count += low
# print(count)

#
# n = int(input())
# if n < 2:
#     print(0)
#     print(n)
# else:
#     dp = [float('inf')] * (n+1)
#     dp[1] = 0
#     path = [-1] * (n+1)
#     for i in range(2, n+1):
#         if dp[i - 1] + 1 < dp[i]:
#             dp[i] = dp[i - 1] + 1
#             path[i] = i - 1
#         if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
#             dp[i] = dp[i // 2] + 1
#             path[i] = i // 2
#         if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
#             dp[i] = dp[i // 3] + 1
#             path[i] = i // 3
#     print(dp[n])
#     trace = []
#     current = n
#     while current != -1:
#         trace.append(current)
#         current = path[current]
#     print(" ".join(str(t) for t in trace))

# from bisect import bisect_left
# import sys
# data = sys.stdin.readlines()
#
# n = int(data[0])
# arr = list(map(int, data[1].strip().split()))
#
# answer = []  # LIS 길이 계산용
# prev = [-1] * n  # 이전 인덱스를 저장하는 배열
# idx = [-1] * n  # LIS에서의 위치를 저장
#
# # LIS 계산
# for i, a in enumerate(arr):
#     lo = bisect_left(answer, a)  # 현재 원소가 들어갈 위치
#     if lo == len(answer):  # 새 원소 추가
#         answer.append(a)
#         if lo > 0:
#             prev[i] = idx[lo - 1]  # 이전 인덱스 저장
#         idx[lo] = i  # 현재 위치 저장
#     else:  # 기존 원소 대체
#         answer[lo] = a
#         if lo > 0:
#             prev[i] = idx[lo - 1]
#         idx[lo] = i
# # LIS 복원
# lis_length = len(answer)
# current = idx[lis_length - 1]
# lis = []
# while current != -1:
#     lis.append(arr[current])
#     current = prev[current]
# lis.reverse()
#
# # 출력
# print(lis_length)
# print(" ".join(map(str, lis)))

# a = str(input().strip())
# b = str(input().strip())
# len_a = len(a)
# len_b = len(b)
# dp = [[""] * (len_a + 1) for _ in range(len_b + 1)]
#
# for i in range(1, len_b + 1):
#     for j in range(1, len_a + 1):
#         if a[j - 1] == b[i - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + a[j - 1]
#         else:
#             if len(dp[i - 1][j]) < len(dp[i][j - 1]):
#                 dp[i][j] = dp[i][j - 1]
#             else:
#                 dp[i][j] = dp[i - 1][j]
#
# print(len(dp[len_b][len_a]))
# print(dp[len_b][len_a])

# import heapq
#
# def hide_and_seek_3_dijkstra(n, k):
#     if k == n:
#         return 0, [n]
#     elif k < n :
#         return n-k, [i for i in range(n, k-1, -1)]
#     # 최대 위치
#     max_pos = 100000
#     # 최단 거리 배열
#     distances = [float('inf')] * (max_pos + 1)
#     distances[n] = 0  # 시작 위치는 0초
#
#     # 우선순위 큐
#     q = []
#     k_time = -1
#     k_route = [n]
#     heapq.heappush(q, (0, n, k_route))  # (거리, 위치)
#     while q:
#         current_time, current_pos, route = heapq.heappop(q)
#
#         # 이미 처리된 노드라면 무시
#         if current_pos == k:
#             k_time = current_time
#             k_route = route
#             break
#
#         # 순간이동
#         next_pos = current_pos * 2
#         if 0 <= next_pos <= max_pos and current_time < distances[next_pos]:
#             distances[next_pos] = current_time
#             new_route = route[:]
#             new_route.append(next_pos)
#             heapq.heappush(q, (current_time, next_pos, new_route))
#
#         # 걷기
#         for next_pos in [current_pos - 1, current_pos + 1]:
#             if 0 <= next_pos <= max_pos and current_time + 1 < distances[next_pos]:
#                 distances[next_pos] = current_time + 1
#                 new_route = route[:]
#                 new_route.append(next_pos)
#                 heapq.heappush(q, (current_time + 1, next_pos, new_route))
#
#     return k_time, k_route
#
# # 입력
# n, k = map(int, input().split())
# # 출력
# answer, answer_route = hide_and_seek_3_dijkstra(n, k)
#
# print(answer)
# print(" ".join(str(a) for a in answer_route))

"""
D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
"""
# from collections import deque
#
# def d_command(n):
#     return (n * 2) % 10000
#
# def s_command(n):
#     return n - 1 if n > 0 else 9999
#
# def l_command(n):
#     return (n % 1000) * 10 + n // 1000
#
# def r_command(n):
#     return (n % 10) * 1000 + n // 10
#
# # BFS로 최소 명령어 경로를 계산
# def bfs_min_commands(start, end):
#     visited = [False] * 10000
#     queue = deque([(start, "")])
#     visited[start] = True
#
#     while queue:
#         current, path = queue.popleft()
#
#         if current == end:
#             return path
#
#         for command, operation in [("D", d_command), ("S", s_command), ("L", l_command), ("R", r_command)]:
#             next_num = operation(current)
#             if not visited[next_num]:
#                 visited[next_num] = True
#                 queue.append((next_num, path + command))
#
# import sys
# input = sys.stdin.read
# data = input().splitlines()
# t = int(data[0])
#
# # 출력
# results = []
# for i in range(1, t + 1):
#     start, end = map(int, data[i].split())
#     results.append(bfs_min_commands(start, end))
#
# print("\n".join(results))

"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
"""
# from collections import defaultdict
# from heapq import heappop, heappush
# import sys
#
# # inf = 100_000
# def dijkstra(start, end, graph, n):
#     distance = [float('inf')] * (n + 1)
#     q = []
#
#     distance[start] = 0
#     heappush(q, (0, start))
#     parent = [-1] * (n + 1)
#     while q:
#         money, node  = heappop(q)
#         if money > distance[node]:
#             continue
#         for need_money, ne in graph[node]:
#             next_money = money + need_money
#             if next_money < distance[ne]:
#                 distance[ne] = next_money
#                 parent[ne] = node
#                 heappush(q, (next_money, ne))
#     route = []
#     current = end
#     while current != -1:
#         route.append(current)
#         current = parent[current]
#     route.reverse()
#
#     return distance[end], route
#
#
# data = sys.stdin.readlines()
# node_c = int(data[0].strip())
# e = int(data[1].strip())
# edge = [list(map(int, d.strip().split())) for d in data[2:e + 2]]
# start, end = map(int, data[e + 2].strip().split())
#
# graph = defaultdict(list)
# for a, b, c in edge:
#     graph[a].append((c, b))
#
# answer, answer_route = dijkstra(start, end, graph, node_c)
# print(answer)
# print(len(answer_route))
# print(" ".join(str(a) for a in answer_route))


import sys
data = sys.stdin.readlines()
n = int(data[0].strip())
w = int(data[1].strip())
lo = [list(map(int, d.strip().split())) for d in data[2:]]


