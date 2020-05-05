N = int(input())

confer = sorted([list(map(int, input().split())) for _ in range(N)] , key= lambda x:(x[1], x[0]))
next_start = cnt = 0
for s_time, f_time in confer:
    if s_time >= next_start:
        next_start = f_time
        cnt += 1

print(cnt)