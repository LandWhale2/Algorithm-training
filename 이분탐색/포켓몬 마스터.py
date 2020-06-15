n, m = map(int, input().split())

pkmn = []
pkmn_dic = {}

for i in range(n):
    pk = input()
    pkmn.append(pk)
    pkmn_dic[pk] = i + 1

for _ in range(m):
    query = input()

    if query.isdigit():
        print(pkmn[int(query)-1])
    else:
        print(pkmn_dic[query])

