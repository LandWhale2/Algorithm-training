N = int(input())
dp = [1,1]
if N >= 3:
    for i in range(2, N+1):
        dp.append(dp[i-1] + dp[i-2])
print(dp[N-1])