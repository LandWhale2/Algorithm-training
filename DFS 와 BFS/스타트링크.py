from collections import deque

F,S,G,U,D = map(int, input().split())

arr = [0] * F
q = deque()
def bfs():
    q.append(S-1)
    arr[S-1] = 1
    while q:
        node = q.popleft()
        if node == G-1:
            print(arr[node] - 1)
            return 0
        if 0 <= node+U < F and arr[node+U] == 0:
            arr[node+U] = arr[node] + 1
            q.append(node+U)
        if 0 <= node-D < F and arr[node-D] == 0:
            arr[node-D] = arr[node] + 1
            q.append(node-D)
    print("use the stairs")
bfs()
