n = int(input())

arr = [int(input()) for _ in range(n)]

command = []
stack = []
for i in range(1, n+1):
    stack.append(i)
    command.append("+")

    while stack:
        if stack[-1] == arr[0]:
            stack.pop()
            arr.pop(0)
            command.append("-")
        else:
            break
    

if arr:
    print("NO")
else:
    for c in command:
        print(c)