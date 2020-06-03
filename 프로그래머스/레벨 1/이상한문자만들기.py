def solution(s):
    s = list(s)
    idx = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if idx % 2 == 0:
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
            idx += 1
        else:
            idx = 0
    return ''.join(s)