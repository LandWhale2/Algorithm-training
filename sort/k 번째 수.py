




def solution(array, commands):
    
    answer = []

    for command in commands:
        a = cutArray(array, command[0], command[1])
        a.sort()
        
        answer.append(a[command[2]-1])
    
    
    return answer



def cutArray(array, start, end):
    list = array[start-1:end]
    
    return list





if __name__ == "__main__":
    solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])