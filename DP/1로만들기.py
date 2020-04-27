import copy

N = int(input())


dp = set()
dp.add(N)
count = 0

def asd(X):
    dp.add(X-1)
    
    if X % 3 == 0:
        dp.add(X//3)
    
    if X % 2 == 0:
        dp.add(X//2)


while(min(dp)!= 1):
    count += 1
    tmp = copy.copy(dp)
    for n in tmp:
        asd(n)

print(count)