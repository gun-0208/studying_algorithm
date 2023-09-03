import sys
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
graph_reverse = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    s,e,w = map(int,input().split())

    graph[s].append((e,w))
    indegree[e] += 1

    graph_reverse[e].append((s,w))

start, end = map(int,input().split())

max_distance = [0] * (n+1)

q = deque()
q.append(start)

while q:
    node = q.popleft()
    
    for next_node, next_dist in graph[node]:
        max_distance[next_node] = max(max_distance[next_node], max_distance[node] + next_dist)
        
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)

q.clear()
q.append(end)
visited = [False] * (n+1)
visited[end] = True

cnt = 0
while q:
    node = q.popleft()

    for prev_node, prev_dist in graph_reverse[node]:
        if max_distance[node] == max_distance[prev_node] + prev_dist:
            cnt += 1
            if not visited[prev_node]:
                visited[prev_node] = True
                q.append(prev_node)

print(max_distance[end])
print(cnt)

