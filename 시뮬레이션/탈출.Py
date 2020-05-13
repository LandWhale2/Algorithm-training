from collections import deque
R,C = map(int,input().split())
arr = [list(map(str, input())) for _ in range(R)]
dx = (-1,0,1, 0)
dy = (0,1, 0, -1)
c = [[0]*C for _ in range(R)]


wq = deque()
q = deque()

def bfs():
    x,y = q[0]
    arr[x][y] = '.'
    c[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<R and 0<=ny<C:
                    if arr[nx][ny] =='.' and c[nx][ny] == 0:
                        c[nx][ny] = c[x][y] + 1
                        q.append((nx, ny))
                    elif arr[nx][ny] =='D':
                        print(c[x][y])
                        return
            qlen -= 1
        water()
    print("KAKTUS")
    return



def water():
    wqlen = len(wq)
    while wqlen:
        x,y = wq.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0<=nx<R and 0<=ny<C and arr[nx][ny] =='.':
                arr[nx][ny] = '*'
                wq.append((nx,ny))
        wqlen -= 1
                


for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            wq.append((i,j))
        elif arr[i][j] == 'S':
            q.append((i,j))




water()
bfs()