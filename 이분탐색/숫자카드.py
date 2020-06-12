def find(n, arr,left, right):
    if left > right:
        return False
    mid = (left+right) // 2
    if arr[mid] > n:
        return find(n, arr, left, mid-1)
    elif arr[mid] < n:
        return find(n, arr, mid+1, right)
    else:
        return True

N = int(input())
cards = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
cards.sort()
res = []

for i in arr:
    if find(i, cards, 0, N-1):
        res.append(1)
    else:
        res.append(0)

print(*res)
