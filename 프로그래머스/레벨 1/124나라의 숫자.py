def asd(n):
    tmp = ''
    while n > 0:
        n -= 1
        tmp = '124'[n%3] + tmp
        n //= 3
    return tmp

def solution(n):
    return asd(n)