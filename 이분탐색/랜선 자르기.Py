k, n = map(int, input().split())
arr = [int(input()) for i in range(k)]

left = 1
right = max(arr)

while left <= right:
    mid = (left+right) // 2
    res = 0
    for i in arr:
        res += i//mid
    
    if res >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)