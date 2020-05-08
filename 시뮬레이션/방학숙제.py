l,a,b,c,d = int(input()),int(input()),int(input()),int(input()),int(input())
ll = l
while l > 0:
    l -= 1
    a -= c
    b -= d
    if a <= 0 and b <= 0:
        break
    

print(l)