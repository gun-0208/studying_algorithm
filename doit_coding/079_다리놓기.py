import sys
input = sys.stdin.readline

dp = [[0 for _ in range(31)] for _ in range(31)]

for i in range(31):
    dp[i][0] = 1
    dp[i][i] = 1
    dp[i][1] = i

for i in range(2,31):
    for j in range(1,i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for _ in range(int(input())):
    n,m = map(int,input().split())

    print(dp[m][n])