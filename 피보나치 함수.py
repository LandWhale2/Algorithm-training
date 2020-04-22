T = int(input())

Zero = [1, 0, 1]
One = [0, 1, 1]


def asd(n):
    length = len(Zero)
    if length <= n:
        for i in range(length, n+1):
            Zero.append(Zero[i-1] + Zero[i-2])
            One.append(One[i-1] + One[i-2])
            
    print("%d %d"%(Zero[n],One[n]))
        
    


for n in range(T):
    N = int(input())
    asd(N)