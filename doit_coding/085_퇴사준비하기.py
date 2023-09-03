import sys
input = sys.stdin.readline

n = int(input())

T = [0] * (n+1)
P = [0] * (n+1)

for i in range(1,n+1):
    T[i], P[i] = map(int,input().split())

dp = [0] * (n+2)
dp[n+1] = 0

for i in range(n,0,-1):
    if i + T[i] > n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+T[i]] + P[i])

print(dp[1])