N,M = map(int, input().split())
x,y,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = (-1,0,1,0)
dy = (0,1,0,-1)

cnt = 1
arr[x][y] = 2
while True:
    check = False
    for i in range(4):
        dd = (d+3) % 4
        nx, ny = x + dx[dd], y + dy[dd]
        d = dd
        if arr[nx][ny] == 0:
            arr[nx][ny] = 2
            cnt += 1
            check = True
            x,y = nx,ny
            break
    if check == False:
        if arr[x-dx[d]][y-dy[d]] == 1:
            break
        else:
            x,y = x-dx[d], y-dy[d]

print(cnt)