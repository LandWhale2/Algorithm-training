N = input()

N = sorted(N ,reverse = True)

result = 0
if '0' not in N:
    print(-1)
else:
    for i in N:
        result += int(i)
    
    if result % 3 != 0:
        print(-1)
    else:
        print(''.join(N))

