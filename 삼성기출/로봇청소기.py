N,M = map(int,input().split())
x,y,d = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr[x][y] = 2

dx = (-1,0,1,0)
dy = (0,1,0,-1)

while True:
    check = False
    for i in range(4):
        dd = (d+3) % 4
        nx, ny = x+dx[dd], y+dy[dd]
        d = dd
        if arr[nx][ny] == 0:
            arr[nx][ny] = 2
            x,y = nx,ny
            check = True
            break
    
    if check == False:
        if arr[x-dx[d]][y-dy[d]] == 1:
            break
        else:
            x,y = x-dx[d],y-dy[d]

cnt = 0
for a in arr:
    cnt += a.count(2)

print(cnt)