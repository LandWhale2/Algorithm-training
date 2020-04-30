N, M, V = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N + 1)]


for i in range(M):
    x, y = map(int, input().split())
    arr[x][y] = arr[y][x] = 1



def dfs(node, arrr, result):
    result.append(node)
    for i in range(len(arrr[node])):
        if arrr[node][i] and i not in result:
            dfs(i, arrr, result)
    return result


def bfs(s):
    q = [s]
    result = [s]

    while(q):
        node = q.pop(0)
        for i in range(len(arr[node])):
            if arr[node][i] and i not in result:
                result.append(i)
                q.append(i)
    return result

print(*dfs(V, arr, []))
print(*bfs(V))
