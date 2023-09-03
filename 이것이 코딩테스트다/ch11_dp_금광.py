result = []

for _ in range(int(input())):
    n,m = map(int,input().split())
    data = list(map(int,input().split()))
    array = []
    dp = [[-1] * m for _ in range(n)]

    for i in range(0,n):
        array.append(data[i*m:i*m+m])

    for i in range(n):
        dp[i][0] = array[i][0]

    for j in range(1,m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            left = dp[i][j-1]

            dp[i][j] = array[i][j] + max(left_up,left_down,left)
    maximum = 0

    for i in range(n):
        if maximum < dp[i][m-1]:
            maximum = dp[i][m-1]
    result.append(maximum)

for max_num in result:
    print(max_num)
