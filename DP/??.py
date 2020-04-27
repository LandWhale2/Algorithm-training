
n = int(input())

dp = []

for i in range(n):
    if i==0:
        dp.append(1)
    else:
        dp.append(dp[i-1] + dp[i-2]*2)
    

print(dp[n-1] % 10007)