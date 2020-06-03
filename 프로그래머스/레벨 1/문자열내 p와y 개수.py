from collections import Counter
def solution(s):
    a = Counter(s.upper())
    if a['Y'] == a['P']:
        return True
    else:
        return False