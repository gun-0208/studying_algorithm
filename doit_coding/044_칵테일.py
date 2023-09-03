def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
def DFS(node):
    visited[node] = True

    for next in graph[node]:
        next_node = next[0]

        if not visited[next_node]:
            D[next_node] = D[node] * next[2]//next[1]
            DFS(next_node)

n = int(input())

graph = [[] for _ in range(n)]
lcm = 1
visited = [False] * n
for _ in range(n):
    a,b,p,q = map(int,input().split())

    graph[a].append((b,p,q))
    graph[b].append((a,p,q))

    lcm *= (p*q // gcd(p,q))

D = [0] * n
D[0] = lcm

DFS(0)

mgcd = D[0]

for i in range(1,n):
    mgcd = gcd(mgcd,D[i])

for i in range(n):
    print(int(D[i]//mgcd), end=" ")
