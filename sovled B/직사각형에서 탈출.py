x,y,w,h = map(int, input().split())

nx, ny = abs(x-w), abs(y-h)

print(min(nx,ny,x,y))

