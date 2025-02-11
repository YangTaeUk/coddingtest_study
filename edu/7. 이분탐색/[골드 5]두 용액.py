n = int(input())
arr = list(map(int, input().strip().split()))

arr.sort()
left, right  = 0, n-1
min_left, min_right = 0, 0
min_sum = float('inf')

while left < right:
    arr_sum = arr[left]+arr[right]
    if abs(arr_sum) < min_sum:
        min_sum = abs(arr_sum)
        min_left = arr[left]
        min_right = arr[right]

    if arr_sum == 0:
        break
    elif arr_sum < 0:
        left += 1
    elif arr_sum > 0:
        right -= 1

print(min_left, min_right)



