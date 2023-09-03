n = int(input())
memo = [-1] * (n+1)

def fib(n):

    if n == 1 or n == 2:
        return 1
    
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

dp = [-1] * (n+1)
cnt2 = 0

def fibo_dp(n):
    global cnt2
    dp[1] = dp[2] = 1

    for i in range(3,n+1):
        cnt2 += 1
        dp[i] = dp[i-1] + dp[i-2]    

    return dp[n]
fibo_dp(n)
print(fib(n))
print(cnt2)