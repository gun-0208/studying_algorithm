# 1,1,2,3,5,8,13,21,...로 이어가는 피보나치 수열의 점화식은 a(n) = a(n-1) + a(n-2)이다.
# 해당 점화식을 재귀함수를 이용하면 쉽게 풀 수 있으나, 재귀함수의 연산과정에서 중간중간 중복계산되는 부분이 너무 많아진다.
# 최종 답을 구하기 위해 앞 전에 연산되었던 서브 결과들을 메모 해놓고 중복된 연산이 뜰때마다 해당 값을 참조하도록 하면 연산을 안해도 될것이다.

n = int(input())

d = [0] * (n+1)

def fibo_dynamic(x):
    if x==1 or x==2:
        return 1
    
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo_dynamic(x-1) + fibo_dynamic(x-2)
    return d[x]

print(fibo_dynamic(n))