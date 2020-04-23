T = int(input())

def asd(n):
    dp = [1, 1, 1, 2, 2]
    if n < 6:
        print(dp[n-1])
    else:
        for i in range(5, n+1):
            dp.append(dp[i-1] + dp[i-5])
        print(dp[n-1])
        


for _ in range(T):
    asd(int(input()))