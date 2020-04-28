N, M = map(int, input().split())

dp = [[0 for i in range(M+1)]] 
for i in range(N):
    dp.append([0] + list(map(int, input().split())))


for i in range(1 ,N+1):

    for j in range(1, M+1):
        dp[i][j] += max(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])

print(max(dp[i]))