N = int(input())
board = [[1] * 101 for _ in range(101)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]


for i in range(N):
    x,y,d,g = map(int, input().split())
    curve_info = [d]
    for i in range(g):
        curve_info += [(i+1)%4 for i in curve_info[::-1]]
    board[y][x] = 0
    nx = x
    ny = y
    for dd in curve_info:
        nx = nx + dy[dd]
        ny = ny + dx[dd]
        board[ny][nx] = 0

cnt = 0
for i in range(100):
    for j in range(100):
        if not board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]:
            cnt += 1

print(cnt)