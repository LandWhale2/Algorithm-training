import re
def solution(dartResult):
    bonusP = {'S':1, 'D': 2, 'T':3}
    option = {'*':2,'#': -1, '': 1}
    p = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    s = p.findall(dartResult)
    for i,score in enumerate(s):
        point, bonus, op = score
        if op == '*' and i > 0:
            s[i-1] *= 2
        s[i] = int(int(point) ** bonusP[bonus]) * option[op]
    return sum(s)