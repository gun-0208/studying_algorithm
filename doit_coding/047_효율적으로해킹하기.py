import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    graph[e].append(s)

hacking_cnts = [0] * (n+1)

def BFS(node):
    visited[node] = True
    q = deque()
    q.append(node)

    while q:
        curr_node = q.popleft()
        for next in graph[curr_node]:
            if not visited[next]:
                visited[next] = True
                hacking_cnts[node] += 1
                q.append(next)

for node in range(1,n+1):
    visited = [False] * (n+1)
    BFS(node)

Max = 0
for i in range(1,n+1):
    Max = max(Max,hacking_cnts[i])

for i in range(1,n+1):
    if hacking_cnts[i] == Max:
        print(i ,end =" ")