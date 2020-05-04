N = int(input())

A = list(map(int, input().split()))


A.sort()
a=0
result=0

for i in range(N):
    a += A[i]
    result += a

print(result)