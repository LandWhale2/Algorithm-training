import math

def solution(s):
    answer = ''
    leng = int(len(s) / 2)

    if (len(s)%2) == 0:
        answer = s[leng-1:leng+1]
    else:
        answer = s[leng]

    
    return answer


if __name__ == "__main__":
    solution("qwer")