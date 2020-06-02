from collections import deque
N,L,R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = (0,0,1,-1)
dy = (1,-1,0,0)






def bfs(x,y):
    global is_check
    q = deque()
    q.append((x,y))
    result = set([(x,y)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0<=nx<N and 0<=ny<N and (nx,ny) not in result and (nx,ny) not in visit:
                gap = abs(arr[nx][ny] - arr[x][y])
                if L <= gap <= R:
                    q.append((nx,ny))
                    result.add((nx,ny))
                    is_check = True
    if len(result) > 1:
        value_sum = sum([arr[i][j] for i,j in result])
        value = value_sum // len(result)
        for x,y in result:
            arr[x][y] = value
        
    
    return result


cnt = 0


while True:
    visit = set()
    is_check = False
    for i in range(N):
        for j in range(len(arr[i])):
            if (i,j) not in visit:
                visited = bfs(i,j)
                visit |= visited
                

    if not is_check:
        break
    cnt += 1
print(cnt)