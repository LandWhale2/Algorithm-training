from collections import deque

N = int(input())

arr = [list(map(int, list(input()))) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


ctn_list = []


def bfs(I,J):
    q = deque()
    q.append((I,J))
    ctn = 1
    arr[I][J] = 0
    while (q):
        x, y = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny]:
                    arr[nx][ny] = 0
                    q.append((nx,ny))
                    ctn += 1
    return ctn



for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            ctn_list.append(bfs(i,j))

print(len(ctn_list))
for i in sorted(ctn_list):
    print(i)