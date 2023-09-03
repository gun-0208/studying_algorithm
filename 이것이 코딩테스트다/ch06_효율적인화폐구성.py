# n 종류의 화폐가 있다.
# 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 m이 되도록 하려고 한다.
# 각 화폐는 몇개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
# 1<= n <= 1,000 , 1<=m<=10,000

n , m = map(int,input().split())

coin_types = []
for _ in range(n):
    coin_types.append(int(input()))

# 10001원은 계산할 수 없으므로 일단 d배열을 m+1의 길이만큼 선언하고 각 값으로 10001원을 저장.
# coin_types를 하나씩 돌면서 해당 인덱스가 계산가능한 값이면 10001에서 계산한 개수로 변경예정.
d = [10001] * (m+1)
d[0] = 0

for coin in coin_types:
    for j in range(coin, m+1):
        if d[j-coin] != 10001:
            d[j] = min(d[j],d[j-coin] + 1)
