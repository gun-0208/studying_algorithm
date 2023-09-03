# 1,1,2,3,5,8,13,...로 이어지는 피보나치 수열이 있을 때

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))