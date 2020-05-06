N, M = map(int, input().split())
p = 1001
t = 1001
result = 0
for i in range(M):
    tmplist = list(map(int, input().split()))
    p = min(p, tmplist[0])
    t = min(t, tmplist[1])


if N > 6:
    remainder = N // 6
    quotient = N % 6
    res = [p * (remainder+1), remainder*p + quotient*t, N * t]
    result = min(res)
else:
    result = min(p, t*N)

print(result)