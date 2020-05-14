from collections import deque


dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    cnt = 1
    arr[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1
    
    result.append(cnt)
    return





M,N,K = map(int, input().split())

arr = [[0] * N for _ in range(M)]
for k in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1



result = []

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            bfs(i,j)

result.sort()
print(len(result))
print(*result)
