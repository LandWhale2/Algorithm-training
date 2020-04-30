C = int(input())
M = int(input())
arr = [[0]*(C+1) for _ in range(C+1)]
for i in range(M):
    x, y = map(int, input().split())
    arr[x][y] = arr[y][x] = 1


def bfs():
    result = [1]
    q = [1]
    while(q):
        node = q.pop(0)

        for i in range(len(arr[node])):
            if arr[node][i] and i not in result:
                q.append(i)
                result.append(i)
    return result


print(len(bfs()) - 1)

