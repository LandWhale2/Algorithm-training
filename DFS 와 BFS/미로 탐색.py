from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
# 0 오른쪽
# 1 왼쪽
# 2 아래쪽
# 3 위쪽
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
q = deque()
check = [[False] * M for _ in range(N)]
result = [[0] * M for _ in range(N)]

check[0][0] = True
result[0][0] = 1
q.append((0,0))

while (q):
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if check[nx][ny] == False and maze[nx][ny]:
                q.append((nx,ny))
                result[nx][ny] = result[x][y] + 1
                check[nx][ny] = True

print(result[N-1][M-1])