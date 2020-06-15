from collections import Counter
def check(n, arr, left, right):
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] > n:
            right = mid - 1
        elif arr[mid] < n:
            left = mid + 1
        else:
            return mid
    return -1

    


N = int(input())
cards = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
c = Counter(cards)
cards.sort()
res = [0] * M

for i,v in enumerate(arr):
    idx = check(v, cards, 0, N-1)
    if idx == -1:
        continue
    res[i] = c[v]

print(*res)