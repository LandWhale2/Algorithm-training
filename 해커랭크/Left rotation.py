def rotLeft(a, d):
    a = deque(a)
    a.rotate(-d)
    return a