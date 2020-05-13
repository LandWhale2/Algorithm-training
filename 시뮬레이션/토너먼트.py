N, ji, im = map(int, input().split())
cnt = 0
while ji != im:
    ji -= ji // 2
    im -= im // 2
    cnt += 1

print(cnt)