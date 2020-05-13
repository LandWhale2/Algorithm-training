from collections import deque
M,N = map(int ,input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
dx = (0, 0, 1,-1)
dy = (1, -1, 0, 0)

def bfs():
    check = [[False]*M for _ in range(N)]
    result = 0
    while q:
        result += 1
        for _ in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0 and check[nx][ny] == False:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx,ny))
                    check[nx][ny] = True
    return result

        


for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i,j))


res = bfs() - 1
check_zero = False
for i in range(N):
    if 0 in arr[i]:
        print(-1)
        exit()


print(res)




