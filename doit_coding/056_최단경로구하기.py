import sys
from queue import PriorityQueue

input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    s,e,w = map(int,input().split())

    graph[s].append((e,w))

min_dist = [1e9] * (V+1)
min_dist[start] = 0

q = PriorityQueue()
q.put((0,start))

visited = [False] * (V+1)

while q.qsize() > 0:
    dist, node = q.get()

    if visited[node] == True:
        continue

    visited[node] = True
    for next_node, next_dist in graph[node]:
        if min_dist[next_node] > min_dist[node] + next_dist:
            min_dist[next_node] = min_dist[node] + next_dist
            q.put((min_dist[next_node], next_node))

for i in range(1,V+1):
    if visited[i]:
        print(min_dist[i])
    else:
        print("INF")

