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

depth = [0] * (n+1)
parent = [0] * (n+1)
visited = [False] * (n+1)

def BFS(node):
    visited[node] = True
    q = deque()
    q.append(node)
    level = 1
    now_size = 1
    count = 0

    while q:
        curr_node = q.popleft()
        
        for next in tree[curr_node]:
            if not visited[next]:
                visited[next] = True
                parent[next] = curr_node
                depth[next] = level
                q.append(next)
        count += 1
        if now_size == count:
            count = 0
            now_size = len(q)
            level += 1
        
BFS(1)

def LCA(a,b):
    if depth[a] < depth[b]:
        temp = a
        a = b
        b = temp

    while depth[a] != depth[b]:
        a = parent[a]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    print(str(LCA(a,b)))
    print("\n")
        