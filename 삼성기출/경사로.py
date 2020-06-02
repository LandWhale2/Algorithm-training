N,L = map(int,input().split())
arrs = [list(map(int, input().split())) for _ in range(N)]



def checkroad(heights):
    visited = [False for i in range(N)]    
    current = heights[0]
    for i, height in enumerate(heights):
        if current == height:
            continue
        elif current+1 == height:
            for j in range(i-1, i-1-L, -1):
                if j < 0 or current != heights[j] or visited[j] == True:
                    return False
                visited[j] = True
            current = height
        elif current-1 == height:
            for j in range(i, i+L):
                if j >= N or current-1 != heights[j] or visited[j] == True:
                    return False
                visited[j] = True
            current = height
        else:
            return False
    return True

cnt = 0
for j in range(N):
    road = []
    for i in range(N):
        road.append(arrs[i][j])
    if checkroad(road):
        cnt += 1

for i in range(N):
    if checkroad(arrs[i]):
        cnt += 1

print(cnt)