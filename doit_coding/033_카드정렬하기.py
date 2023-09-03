import heapq

n = int(input())
queue = []
for _ in range(n):
    queue.append(int(input()))

heapq.heapify(queue)

count = 0
while len(queue) > 1:
    num1 = heapq.heappop(queue)
    num2 = heapq.heappop(queue)

    # 합쳐진 카드 갯수
    unioned = num1+num2

    # 카드를 합치는데 든 횟수
    count += unioned

    # 합친 카드를 다시 합치기 위해 큐에 추가
    queue.append(unioned)
    

print(count)

