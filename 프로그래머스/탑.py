def solution(heights):
    answer = []
    leng = len(heights)
    
    a = [0] * leng
    
    

    for i in range(len(heights)-1, -1 , -1):
        
        for j in range(i-1, -1 , -1):
            if heights[i] < heights[j]:
                
                a[i] = j+1
                break
    
    return a