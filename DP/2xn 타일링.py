n = int(input())

dp = [1,2]


length = len(dp)

if length <= n:
    for i in range(length, n+1):
        dp.append(dp[i-1] + dp[i-2])

print(dp[n-1] % 10007)