N, L = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

t_index = 0
cnt = 0
for i in arr:
    if i > t_index:
        t_index = i + L - 1
        cnt += 1
print(cnt)