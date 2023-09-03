from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    s,e = map(int,input().split())

    graph[s].append(e)
    indegree[e] += 1

q = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    print(node, end=" ")
    
    for next in graph[node]:
        indegree[next] -= 1
        
        if indegree[next] == 0:
            q.append(next)
            