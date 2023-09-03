import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int,input().split()))
del_node = int(input())

root_node = -1
for i in range(n):
    if parent[i] == -1:
        root_node = i

graph = [[] for _ in range(n)]
for i in range(n):
    if parent[i] == -1:
        continue
    graph[i].append(parent[i])
    graph[parent[i]].append(i)

visited = [False] * n
cnt_leaf = 0
def DFS(node):
    global cnt_leaf

    visited[node] = True
    child_node = 0

    for next in graph[node]:
        if not visited[next] and next != del_node:
            visited[next] = True
            child_node += 1
            DFS(next)
    
    if child_node == 0:
        cnt_leaf += 1

DFS(root_node)

if del_node == root_node:
    print(0)
else:
    print(cnt_leaf)

