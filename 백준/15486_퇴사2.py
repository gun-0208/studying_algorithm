n = int(input())

t = []
p = []
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    t_i,p_i = map(int,input().split())

    t.append(t_i)
    p.append(p_i)

for i in range(n-1,-1,-1):
    time = i + t[i]

    if time <= n:
        dp[i] = max(dp[time] + p[i], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
    
print(max(dp))