import sys
sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

x = [' '] + list(input())
y = [' '] + list(input())

dp = [[0 for _ in range(len(y))] for _ in range(len(x))]
tracking = [[0 for _ in range(len(y))] for _ in range(len(x))]

for i in range(1,len(x)):
    for j in range(1,len(y)):
        if x[i] == y[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            tracking[i][j] = 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            tracking[i][j] = 2 if dp[i][j-1] > dp[i-1][j] else 3

def back_tracking(x,i,j,tracking):
    if i == 0 or j == 0:
        return ""
    
    else:
        if tracking[i][j] == 1:
            return back_tracking(x,i-1,j-1,tracking) + x[i]
        elif tracking[i][j] == 2:
            return back_tracking(x,i,j-1,tracking)
        elif tracking[i][j] == 3:
            return back_tracking(x,i-1,j,tracking)

print(dp[len(x)-1][len(y)-1])
print(back_tracking(x,len(x)-1,len(y)-1,tracking))
             