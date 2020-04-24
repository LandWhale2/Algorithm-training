N = int(input())

dp = [[0]*10 for _ in range(N+1)]



for i in range(0,10):
    dp[0][i] = 1

for i in range(1 ,N+1):
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]


print(dp[N][-1] % 10007)