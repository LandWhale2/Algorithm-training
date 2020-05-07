from collections import deque
N = int(input())

card = deque(list(range(1,N+1)))

while card:
    if len(card) == 1:
        break
    card.popleft()
    value = card.popleft()
    card.append(value)

print(card[0])