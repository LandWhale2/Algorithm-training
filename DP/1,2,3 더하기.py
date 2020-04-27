T = int(input())

dp = [1, 2, 4] + [0]*8


def asd(N):

    if N <= 3:
        print(dp[N-1])
    else:
        
        for i in range(3, N+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[N-1])

for i in range(T):
    asd(int(input()))
