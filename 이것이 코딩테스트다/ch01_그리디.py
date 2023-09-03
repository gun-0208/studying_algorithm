# 거스름돈 개수 최소한으로 거슬러주기
# 코인 타입 : [500,100,50,10]

n = 1260
coin_types = [500,100,50,10]

cnt = 0

for coin in coin_types:
    cnt += n // coin
    n %= coin
    print(f"coin : {coin} , cnt : {cnt}")

print("result" , cnt) 