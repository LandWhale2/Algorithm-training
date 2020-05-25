from collections import deque
n,k = int(input()),int(input())
board = [[0]*n for _ in range(n)]
for i in range(k):
    x,y = map(int, input().split())
    board[x-1][y-1] = 2

l = int(input())
command = [[0,0]] * 10000
for i in range(l):
    a, d = input().split()
    command[i] = [int(a), d]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
x,y = 0,0
idx = 0
cnt = 0
q = deque()
board[x][y] = 1
q.append((0,0))
d = 0
while True:
    if cnt == command[idx][0] and len(command) > idx:
        dd = command[idx][1]
        idx += 1
        if dd == 'D':
            d = (d+1)%4
        elif dd == 'L':
            d = (d-1)%4
    nx = x + dx[d]
    ny = y + dy[d]
    if 0<=nx<n and 0<=ny<n and board[nx][ny] != 1:
        if board[nx][ny] == 2:
            q.append((nx,ny))
            board[nx][ny] = 1
            x, y = nx, ny
        elif board[nx][ny] == 0:
            q.append((nx,ny))
            xx, yy = q.popleft()
            board[xx][yy] = 0
            board[nx][ny] = 1
            x,y = nx,ny
        cnt += 1
    else:
        cnt += 1
        print(cnt)
        break