N = int(input())
dp = [0] * 1000
for i in range(N):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = 3
    else:
        dp[i] = dp[i-2] * 2 + dp[i-1]
print(dp[N-1] % 10007)