def asd(arr):
    max_ = -10e5
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum_ = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            max_ = max(max_, sum_)
    print(max_)



aa = [[i for i in range(1,10)] for _ in range(9)]
print(asd(aa))