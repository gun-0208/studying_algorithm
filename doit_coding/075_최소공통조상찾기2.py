import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    s,e = map(int,input().split())
    tree[s].append(e)
    tree[e].append(s)

kmax = 0
temp = 1

while temp <= n:
    temp <<= 1
    kmax += 1

parent = [[0 for _ in range(n+1)] for _ in range(kmax+1)]
visited = [False] * (n+1)
depth = [0] * (n+1)

def BFS(node):
    visited[node] = True
    q = deque()
    q.append(node)
    level = 1
    count = 0
    now_size = 1

    while q:
        curr_node = q.popleft()
        
        for next in tree[curr_node]:
            if not visited[next]:
                visited[next] = True
                depth[next] = level
                parent[0][next] = curr_node
                q.append(next)

        count += 1

        if count == now_size:
            level += 1
            count = 0
            now_size = len(q)
    
BFS(1)
for k in range(1,kmax+1):
    for node in range(1,n+1):
        parent[k][node] = parent[k-1][parent[k-1][node]]

def executeLCA(a,b):
    if depth[a] > depth[b]:
        temp = a
        a = b
        b = temp
    
    for k in range(kmax,-1,-1):
        if pow(2,k) <= depth[b] - depth[a]:
            if depth[a] <= depth[parent[k][b]]:
                b = parent[k][b]

    for k in range(kmax,-1,-1):
        if a == b:
            break
        
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    LCA = a

    if a != b:
        LCA = parent[0][LCA]
    
    return LCA

m = int(input())

for _ in range(m):
    a,b = map(int,input().split())

    print(str(executeLCA(a,b)))
    print("\n")

