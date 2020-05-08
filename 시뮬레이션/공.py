N = int(input())

cups = [list(map(int, input().split())) for i in range(N)]
arr = [0]*4
arr[1] = 1


for cup1, cup2 in cups:
    arr[cup1], arr[cup2] = arr[cup2], arr[cup1]

print(arr.index(1))