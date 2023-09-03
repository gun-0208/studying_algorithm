# M번의 합을 하는데 같은 수를 K번까지만 반복해서 더할 수 있음.
# 숫자 리스트 중에서 가장 큰값을 찾아 K번 더하고, K+1번째에서는 두번 째로 큰 값을 더함.
# cnt가 M이 될 때 까지 계속해서 반복

n,m,k = map(int,input().split())
num_list = list(map(int,input().split()))

max = 0 
max_idx = 0
for idx, value in enumerate(num_list):
    if value > max:
        max = value
        max_idx = idx

max_2 = 0
for idx,value in enumerate(num_list):
    if max_idx == idx:
        continue

    if value > max_2:
        max_2 = value

result =  (max * k + max_2 * 1) * m//(k+1) + (max * m%(k+1))
print(result)