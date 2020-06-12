def find(n, arr, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > n:
            right = mid - 1
        elif arr[mid] < n:
            left += 1
        else:
            return True
    return False



n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for nn in m_list:
    if find(nn, n_list, 0, n-1):
        print(1)
    else:
        print(0)