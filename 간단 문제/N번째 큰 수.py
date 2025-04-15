


import sys, heapq
data = sys.stdin.readlines()

T = int(data[0].strip())
heap = []

for i in range(1, T + 1):
    for num in map(int, data[i].strip().split()):
        heapq.heappush(heap, num)
        if len(heap) > T:
            heapq.heappop(heap)

print(heapq.heappop(heap))  # T번째로 큰 수