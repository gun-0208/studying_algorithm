from collections import deque

n,m,start = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort()

def DFS(node):
    visited[node] = True
    print(node, end=" ")

    for next in graph[node]:
        if not visited[next]:
            DFS(next)

def BFS(node):
    visited[node] = True
    
    q = deque()
    q.append(node)
    
    while q:
        curr_node = q.popleft()
        print(curr_node, end=" ")

        for next in graph[curr_node]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

visited = [False] * (n+1)
DFS(start)
print()
visited = [False] * (n+1)
BFS(start)