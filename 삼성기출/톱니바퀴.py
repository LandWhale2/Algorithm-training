from collections import deque

arr = [deque(list(map(int, input()))) for _ in range(4)]

k = int(input())
for i in range(k):
    n,d = map(int, input().split())
    command = [0] * 4
    command[n-1] = d
    for j in range(n-1,3):
        if arr[j][2] != arr[j+1][6]:
            command[j+1] = -command[j]
    
    for j in range(n-1, 0, -1):
        if arr[j][6] != arr[j-1][2]:
            command[j-1] = -command[j]
    
    for j in range(4):
        if command[j] == 1:
            arr[j].rotate(1)
        elif command[j] == -1:
            arr[j].rotate(-1)

res = 0

for i in range(4):
    if arr[i][0] == 1:
        res += (1 << i)

print(res)