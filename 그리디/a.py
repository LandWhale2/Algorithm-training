a = input()
b = input()

node = 0
cnt = 0
while node+len(b) <= len(a):
    if a[node:node+len(b)] == b:
        cnt += 1
        node += len(b)
    else:
        node += 1
    


print(cnt)