# 정수 x가 주어질 때, 정수 x에 사용할 수 있는 연산 4가지.
# x가 5로 나누어 떨어지면 5로나눔, x%3 ==0 이면 3으로 나눔 ,x%2==0이면 2로 나눔., x에서 1을 뺌.
# 해당 연산을 이용해서 주어진 수를 1로 만드려고 할 때, 사영하는 연산의 최소 횟수?

# 26은 2로 나누거나, 1을 빼는 연산을 할 수 있다.
# 13은 1을 빼는 연산을 할 수 있고, 25는 5로 나누는 연산을 할 수 있다.
# 처음 주어진 수에서 할 수 있은 연산을 케이스별로 나눠서 시행하고, 그 케이스들 중에서 카운트가 최소인 것을 선정하면 되는데,
# 그 중에는 앞전에서 연산되어야할 숫자들이 포함되어 있다. 이를 동적계획법으로 해결하면 된다.
# 1<= x <= 30,000
x = int(input())

d = [0] * 30001

for i in range(2,x+1):
    # 1을 빼는 경우.
    # 어떤 연산을 하든 해당 연산의 횟수 1이 추가되어야 함.
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
print(d[x])