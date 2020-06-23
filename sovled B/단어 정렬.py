n = int(input())

words = [input() for _ in range(n)]

words = sorted(words, key=lambda x:(len(x), x))
unique = []
for w in words:
    if w not in unique:
        print(w)
        unique.append(w)