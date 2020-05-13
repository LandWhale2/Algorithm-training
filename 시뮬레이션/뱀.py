

dx = (0,1,0,-1)
dy = (1,0,-1,0)

def change(d,c):
    if c == 'L':
        return (d-1)%4
    elif c == 'D':
        return (d+1)%4




N = int(input())
board = [[0]*N for _ in range(N)]
K = int(input())
for i in range(K):
    x,y = map(int ,input().split())
    board[x-1][y-1] = 2

L = int(input())
info = [[0,0]] * 10000
for i in range(L):
    x,c = map(str, input().split())
    info[i] = [int(x), c]

bam = [(0,0)]
board[0][0] = 1
cnt = 0
idx = 0
x,y = 0,0
d = 0
while True:
    if info[idx][0] == cnt:
        d = change(d, info[idx][1])
        idx += 1
    
    nx, ny = x + dx[d], y + dy[d]

    if 0<=nx<N and 0<=ny<N and not board[nx][ny] == 1:

        if board[nx][ny] == 0:
            tx, ty = bam.pop(0)
            board[tx][ty] = 0
        
        bam.append((nx,ny))
        board[nx][ny] = 1
        x,y =nx, ny
        cnt += 1
    else:
        cnt += 1
        break

print(cnt)