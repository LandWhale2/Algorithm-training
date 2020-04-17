def solution(priorities, location):
    answer = 0
    location_index = location
    while(priorities):
        if max(priorities) > priorities[0]:
            if location_index == 0:
                location_index = len(priorities) - 1
            else:
                location_index -= 1
            value = priorities.pop(0)
            priorities.append(value)
        else:
            priorities.pop(0)
            answer += 1
            if location_index == 0:
                return answer
            else:
                location_index -= 1
    
    return answer