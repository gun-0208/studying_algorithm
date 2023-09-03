from collections import deque
import sys

input = sys.stdin.readline
n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,input().split())

    graph[u].append(v)

visited = [False] * (n+1)
distance = [-1] * (n+1)

def BFS(node):
    visited[node] = True
    distance[node] = 0

    q = deque()
    q.append(node)

    while q:
        curr_node = q.popleft()
        for next_node in graph[curr_node]:
            if not visited[next_node]:
                visited[next_node] = True
                distance[next_node] = distance[curr_node] + 1
                q.append(next_node)


BFS(x)

answer = []
for i in range(1,n+1):
    if distance[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)