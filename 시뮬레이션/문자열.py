a, b = map(str, input().split())

add =0
result = 50
while len(a) + add <= len(b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i+add]:
            cnt += 1
    result = min(result, cnt)
    add += 1

print(result)