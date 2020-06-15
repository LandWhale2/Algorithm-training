N = int(input())
arr = list(map(int, input().split()))
M = int(input())

left = 0
right = max(arr)

while left <= right:
    mid = (left + right) // 2
    res = 0
    for i in arr:
        if mid >= i:
            res += i
        else:
            res += mid
    
    if res > M:
        right = mid - 1
    elif res < M:
        left = mid + 1
    else:
        right = mid
        break

print(right)