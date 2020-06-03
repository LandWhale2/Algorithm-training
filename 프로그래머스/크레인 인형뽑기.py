def solution(board, moves):
    answer = 0
    idx = 0
    stack = []
    while idx < len(moves):
        mov_idx = moves[idx] - 1
        for i in range(len(board)):
            item = board[i][mov_idx]
            if item != 0:
                stack.append(item)
                board[i][mov_idx] = 0
                break
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
        idx += 1
        
    return answer