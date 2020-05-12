from collections import deque
N,M = map(int, input().split())

target = deque(list(map(int, input().split())))

q = deque(list(range(1, N+1)))
cnt = 0
while target:
    if target[0] == q[0]:
        q.popleft()
        target.popleft()
    else:
        if q.index(target[0]) <= len(q)//2:
            while q[0]!=target[0]:
                q.rotate(-1)
                cnt += 1
        else:
            while q[0]!=target[0]:
                q.rotate(1)
                cnt += 1

print(cnt)