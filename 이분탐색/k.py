from math import floor
x,y = map(int, input().split())
left, right = 1, 1000000000
origin = floor(100 * y / x)

if origin >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        tx = x + mid
        ty = y + mid
        new_rating = floor(100* ty/ tx)
        if new_rating > origin:
            right = mid - 1
        else:
            left = mid + 1
    print(right+1)


