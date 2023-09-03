# 만들수 없는 금액 중 최솟값
# n개의 동전. n=5, [3,2,1,1,9] 동전이 있을 때 만들 수 없는 최소금액은 8원이다.
# 1 <= n <= 1000
# 각 화폐 단위는 1,000,000이하의 자연수

n = int(input())
moneys = list(map(int,input().split()))

moneys.sort()

target = 1

for money in moneys:
    if money > target:
        break
    target += money

print(target)