arr = [list(map(int, input().split())) for _ in range(4)]

now = 0
top = 0
for down, up in arr:
    now -= down
    now += up
    top = max(top, now)

print(top)
