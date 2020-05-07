a = int(input())
cnt = 0
while a != 0:
    print(a)
    if a % 2 == 1:
        cnt += 1
    a = a // 2
print(cnt)