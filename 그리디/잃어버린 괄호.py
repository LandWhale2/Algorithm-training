arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
    
for i in arr[1:]:
    for j in i.split('+'):
        print(j)
        s -= int(j)
        
print(s)