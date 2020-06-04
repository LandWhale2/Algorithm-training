def numPlayers(k, scores):
    ranks = []
    for score in scores:
        a = (len(scores) - len([1 for i in scores if i <= score])) + 1
        ranks.append(a)
    
    res = len([1 for i in ranks if i <= k]) - scores.count(0)
    return res

###################



def find(word, words, now, max_value):
    if word in words:
        now += 1
        max_value[0] = now
        print(now, max_value[0])
        for i in range(len(word)):
            tmp = word[:i] + word[i+1:]
            find(tmp, words, now, max_value)
        
        return max_value[0]
    else:
        return 0

def longestChain(words):
    words,max_value = set(words), 0
    for word in words:
        max_res = find(word, words, 0, [0])
        max_value = max(max_value, max_res)
    return max_value
    

    return word_list
