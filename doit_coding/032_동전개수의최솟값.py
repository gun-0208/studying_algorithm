n,target = map(int,input().split())

coin_types = []
for _ in range(n):
    coin_types.append(int(input()))

cnt = 0

for i in range(n-1,-1,-1):
    coin = coin_types[i]

    if coin <= target:
        
        cnt += int(target / coin)
        target %= coin

print(cnt)



