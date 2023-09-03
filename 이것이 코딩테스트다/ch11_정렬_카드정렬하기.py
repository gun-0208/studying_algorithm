# [10,20,40] => (10+20) + ((10+20) + 40) = 100 [minimum]
# 첫번쨰 괄호 안에서 두 카드의 값을 더하고, 그 더한 값이 그 후 연산에서 다시 사용되고 있다. => 그 뜻은 두 카드의 연산 값을 다시 리스트에 넣으라는 소리.

import heapq

n = int(input())

heap = []

for _ in range(n):
    data = int(input())

    heapq.heappush(heap,data)

result = 0

while len(heap) != 1:
    a1 = heapq.heappop(heap)
    a2 = heapq.heappop(heap)

    temp_sum = a1 + a2
    result += temp_sum

    heapq.heappush(heap,temp_sum)

print(result)
