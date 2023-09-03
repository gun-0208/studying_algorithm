import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    u,v = map(int,input().split())
    
    graph[u].append(v)
    graph[v].append(u)

result = False

def DFS(node,level):
    global result
    
    if level == 5:
        result = True
        return
    
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            DFS(next_node,level+1)

    visited[node] = False

for node in range(n):
    DFS(node,1)

    if result:
        break

if result:
    print(1)
else:
    print(0)
