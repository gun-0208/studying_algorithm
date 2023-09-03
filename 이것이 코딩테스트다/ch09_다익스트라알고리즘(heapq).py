import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

start = int(input())

visited = [False] * (n+1)

distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    distance[start] = 0

    heapq.heappush(q,(0,start))

    while q:
        now_dist, now_node = heapq.heappop(q)
        
        if distance[now_node] < now_dist:
            continue


        for i in graph[now_node]:
            cost = now_dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])