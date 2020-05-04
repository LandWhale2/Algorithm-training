coins = [500, 100, 50, 10, 5, 1]

money = int(input())

change = 1000 - money
result = 0
for coin in coins:

    if coin <= change:
        n = change // coin
        change -= coin * n
        result += n

print(result)