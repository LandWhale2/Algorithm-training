from collections import deque
N = int(input())

cards = deque(list(range(1,N+1)))

result = []

while cards:
    result.append(cards.popleft())
    cards.rotate(-1)

print(*result)