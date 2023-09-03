import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

start,end = map(int,input().split())

visited = [False] * (n+1)
min_cost = [1e9] * (n+1)
min_cost[start] = 0

q = PriorityQueue()
q.put((0,start))

while q.qsize() > 0:
    node = q.get()[1]

    if visited[node]:
        continue
    visited[node] = True

    for next_node, next_cost in graph[node]:
        if min_cost[next_node] > min_cost[node] + next_cost:
            min_cost[next_node] = min_cost[node] + next_cost
            q.put((min_cost[next_node] , next_node))

print(min_cost[end])
