def solution(x, n):
    arr = [x]
    for i in range(1,n):
        arr.append(arr[i-1]+x)
    return arr