import sys
input = sys.stdin.readline
# n의 범위가 10,000,000이므로 nlogn 알고리즘으로는 풀 수 없고, 원소의 값 범위가 10,000이하인 자연수 이므로 계수정렬을 이용해보자.

n = int(input())
counting_array = [0] * (10001)

for i in range(1,n+1):
    counting_array[int(input())] += 1

for i in range(10001):
    if counting_array[i] > 0:
        for _ in range(counting_array[i]):
            print(i)