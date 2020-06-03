def solution(n):
    seive = [False, False] + [True] * (n-1)
    for i,e in enumerate(seive):
        if e:
            k = i * 2
            while k <= n:
                seive[k] = False
                k += i
    return len([x for (x,y) in enumerate(seive) if y])