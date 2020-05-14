from collections import deque
T = int(input())

dx = (0,0,1,-1)
dy = (1,-1,0,0)

def bfs(x,y,cnt):
    q = deque()
    q.append((x,y))
    arr[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx,ny))
    return cnt + 1



for _ in range(T):
    M,N,K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x,y = map(int, input().split())
        arr[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt = bfs(i,j,cnt)
    
    print(cnt)
