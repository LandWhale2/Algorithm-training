def solution(arr, divisor):
    if len(sorted([i for i in arr if i % divisor == 0])) == 0:
        return [-1]
    else:
        return sorted([i for i in arr if i % divisor == 0])