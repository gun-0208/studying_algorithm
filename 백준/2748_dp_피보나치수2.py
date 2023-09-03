n = int(input())

dp = [0] * (n+1)

def fibo_dp(n):
    if n == 1 or n == 2:
        return 1
    
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = fibo_dp(n-1) + fibo_dp(n-2)
    
    return dp[n]

print(fibo_dp(n))