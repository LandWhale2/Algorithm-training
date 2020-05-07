T = int(input())

for i in range(T):
    
    N, target = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    
    
    while arr:
        if max(arr) == arr[0]:
            cnt += 1
            if target == 0:
                break
            arr.pop(0)
            if target == 0:
                target = len(arr) - 1
            else:
                target -= 1
        else:
            value = arr.pop(0)
            arr.append(value)
            if target == 0:
                target = len(arr) - 1
            else:
                target -= 1
    
    print(cnt)