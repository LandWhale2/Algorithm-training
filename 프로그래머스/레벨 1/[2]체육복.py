def solution(n, lost, reserve):
    answer = 0
    stu = [1]*n
    for i in lost:
        stu[i-1] = 0
    
    for i in sorted(reserve):
        if stu[i-1] == 0:
            stu[i-1] = 1
            continue
        if i > 0 and stu[i-2] == 0:
            stu[i-2] = 1
            continue
        elif i < len(stu)-1:
            stu[i] = 1
            continue
    return stu.count(1)