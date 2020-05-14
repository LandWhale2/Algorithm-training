from collections import deque
N,K = map(int, input().split())
max_ = 100001
arr = [0] * max_

def bfs():
    q = deque([N])
    arr[N] = 1
    cnt = 0
    while q:
        qlen = len(q)
        while qlen:
            x = q.popleft()
            if x == K:
                print(cnt)
            if 0<=(x+1)<max_ and arr[x+1] == 0:
                arr[x+1] = arr[x] + 1
                q.append(x+1)
            if 0<=(x-1)<max_ and arr[x-1] == 0:
                arr[x-1] = arr[x] + 1
                q.append(x-1)
            if 0<=(x*2)<max_ and arr[x*2] == 0:
                arr[x*2] = arr[x] + 1
                q.append(x*2)
            qlen -= 1
        cnt += 1


bfs()