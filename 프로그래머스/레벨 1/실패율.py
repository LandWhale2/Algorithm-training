def solution(N, stages):
    dic = {}
    len_ = len(stages)
    for i in range(1,N+1):
        if len_ != 0:
            count = stages.count(i)
            dic[i] = count / len_
            len_ -= count
        else:
            dic[i] = 0
    
    
    return sorted(dic, key=lambda x: dic[x], reverse=True)