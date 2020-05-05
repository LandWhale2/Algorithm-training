N , K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
coins.sort(reverse = True)
result = 0
for coin in coins:
    if coin <= K:
        remainder = K // coin
        K -= coin * remainder
        result += remainder

print(result)