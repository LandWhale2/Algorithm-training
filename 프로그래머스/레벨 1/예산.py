def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        answer += 1
        if budget < 0:
            answer -= 1
            break
    return answer