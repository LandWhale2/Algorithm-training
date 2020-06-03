from collections import Counter
def solution(participant, completion):
    result =Counter(participant) - Counter(completion)
    result = list(map(str, result))
    return ''.join(result)