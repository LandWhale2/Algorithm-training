def solution(n):
    num = n ** 0.5
    if num % 1 == 0:
        return (num+1) **2
        
    return -1