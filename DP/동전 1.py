n, k = map(int, input().split())

coins = []

for i in range(n):
    coins.append(int(input()))

dp = [0 for i in range(11)]
dp[0] = 1
for i in coins:

    for j in range(i, k+1):
        print(dp)
        dp[j] += dp[j-i]

print(dp)