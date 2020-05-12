A,B,C = map(int, input().split())
max_ = 0
arr = [0] * 101
result = 0
for i in range(3):
    n,m = map(int, input().split())
    max_ = max(max_, m)
    for j in range(n, m):
        arr[j] += 1



for i in range(1, max_ +1):
    if arr[i] == 1:
        result += arr[i] * A
    elif arr[i] == 2:
        result += arr[i] * B
    elif arr[i] == 3:
        result += arr[i] * C

print(result)