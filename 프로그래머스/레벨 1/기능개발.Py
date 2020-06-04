def solution(progresses, speeds):
    answer = []
    while progresses:
        work = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                work += 1
            else:
                break
        if work > 0:
            answer.append(work)
    return answer