def check(s1,s2):
    for ss1,ss2 in zip(s1,s2):
        if ss1 != ss2:
            return False
    return True


def solution(skill, skill_trees):
    new_skill_trees = []
    answer = 0
    for trees in skill_trees:
        tmp = ''
        for s in trees:
            if s in skill:
                tmp += s
        new_skill_trees.append(tmp)
    
    for new in new_skill_trees:
        if check(new, skill):
            answer += 1
    return answer