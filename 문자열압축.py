def solution(s):
    answer = len(s)
    count = 0
    half_index = len(s)//2 + 1
    for i in range(1, half_index):
        last = ''
        result = ''
        for j in range(0, len(s), i):
            cut = s[j:j+i]
            
            if last == cut:
                count += 1
                
                if len(s) % i == 0:
                    if j == len(s)-i:
                        result += str(count) + last
                else:
                    if j == len(s) - (len(s) % i):
                        result += str(count) + last
                
            elif last == '':
                count = 1
                last = cut
            elif last != cut:
                if count > 1:
                    result += str(count) + last
                else:
                    result += last
                
                
                if len(s) % i == 0:
                    if j == len(s)-i:
                        result += cut
                else:
                    if j == len(s) - (len(s) % i):
                        result += cut
                count = 1
                last = cut
        if len(result) < answer:
            answer = len(result)
            
    return answer