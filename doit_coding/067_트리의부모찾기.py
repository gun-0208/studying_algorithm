import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    start, end = map(int,input().split())

    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (n+1)
answer = [0] * (n+1)

def DFS(node):
    visited[node] = True
    
    for next in graph[node]:
        if not visited[next]:
            answer[next] = node
            DFS(next)

DFS(1)

for i in range(2,n+1):
    print(answer[i])