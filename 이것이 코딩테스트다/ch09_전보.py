# n: 도시의 개수, m: 통로의 개수, c : 메세지 보내고자 하는 도시[c노드에서 출발]
# c노드에서 닿을 수 있는 모든 노드의 개수와 모든 노드가 메세지를 받는데 걸린 총 시간? 최대한 빨리. 최대한 많이.
# dijkstra algorithm
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())

distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,cost = map(int,input().split())

    graph[a].append((b,cost))

def dijkstra(start):
    q = []

    distance[start] = 0
    
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = i[1] + dist

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
max_distance = 0
cnt = 0
for i in range(1,n+1):
    if distance[i] != INF:
        cnt += 1
        max_distance = max(max_distance, distance[i])

print(cnt-1, max_distance)


