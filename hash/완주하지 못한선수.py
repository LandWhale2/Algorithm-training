def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2]
    c = [3,3,1,1,2]

    m = {
        1 : 0,
        2 : 0,
        3 : 0,
    }
    
    for i in range(5):
        if a[i] == answers[i]:
            m[1] += 1

        if b[i] == answers[i]:
            m[2] += 1

        if c[i] == answers[i]:
            m[3] += 1
    
    answer = []
    max_value = max(m.values())
    if max_value == m[1]:
        answer.append(1)
    if max_value == m[2]:
        answer.append(2)
    if max_value == m[3]:
        answer.append(3)

    print(answer)


    return answer


if __name__ == "__main__":
    solution([1,3,2,4,2])