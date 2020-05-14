def solution(progresses, speeds):
    answer = []
    while(progresses):
        day = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        while(progresses[0] >= 100):
            progresses.pop(0)
            speeds.pop(0)
            day += 1
            if not progresses:
                break
        
        if day > 0:
            answer.append(day)
        
    return answer