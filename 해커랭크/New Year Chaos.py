def asd(q):
    cnt = 0
    if len(q) == 1:
        return print(0)
    for i in range(len(q)-1):
        for j in range(i, i+2):
            print(q)
            if i == len(q)-1:
                if q[j] > q[j+1]:
                    q[j],q[j+1] = q[j+1],q[j]
                    cnt += 1
            
            if q[j] > q[j+1]:
                q[j],q[j+1] = q[j+1],q[j]
                cnt += 1
    print(q)
    print(cnt)
    if q == list(range(1,len(q)+1)):
        print(cnt)
    else:
        print('Too chaotic')
asd([1,2,5,3,7,8,6,4])




