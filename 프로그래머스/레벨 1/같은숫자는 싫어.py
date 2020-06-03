def solution(arr):
    last = arr[0]
    answer = [last]
    for i in range(1, len(arr)):
        if last != arr[i]:
            last = arr[i]
            answer.append(arr[i])
    return answer