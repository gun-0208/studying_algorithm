import sys

input = sys.stdin.readline

n,t = map(int,input().split())
data = list(map(int,input().split()))

prefix_sum = [0]

temp = 0
for num in data:
    temp += num
    prefix_sum.append(temp)

for _ in range(t):
    start, end = map(int,input().split())

    print(prefix_sum[end] - prefix_sum[start-1])

    