import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dp = [[0 for _ in range(1001)] for _ in range(1001)]

maximum = 0
for i in range(n):
    data = list(input())

    for j in range(m):
        dp[i][j] = int(data[j])
        
        if dp[i][j] == 1 and i > 0 and j > 0:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + dp[i][j]

        if maximum < dp[i][j]:
            maximum = dp[i][j]


print(maximum * maximum)