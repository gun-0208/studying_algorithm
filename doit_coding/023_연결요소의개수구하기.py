import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u,v = map(int,input().split())

    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True

    for next in graph[node]:
        if visited[next] == False:
            dfs(next)

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1

print(cnt)