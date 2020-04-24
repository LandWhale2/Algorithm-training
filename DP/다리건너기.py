def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result




T = int(input())


for i in range(T):
    N, M = map(int, input().split())
    if N==M:
        print(factorial(M) // factorial(N))
    else:
        print(factorial(M) // factorial((M-N)) // factorial(N))