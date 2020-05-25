n = int(input())
arr = list(map(int, input().split()))
ans = 0
p1, p2 = map(int, input().split())

for i in range(n):
    if arr[i] > 0:
        arr[i] -= p1
        ans += 1
    if arr[i] > 0:
        ans += arr[i] // p2
        if arr[i] % p2 != 0:
            ans += 1

print(ans)