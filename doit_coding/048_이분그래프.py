import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(node):
    global isEven

    visited[node] = True

    for next in graph[node]:
        if not visited[next]:
            check[next] = (check[node] +1)%2
            DFS(next)
        else:
            if check[node] == check[next]:
                isEven = False

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    isEven = True
    check = [0] * (n+1)

    for _ in range(m):
        s,e = map(int,input().split())

        graph[s].append(e)
        graph[e].append(s)
    
    for node in range(1,n+1):
        if isEven:
            DFS(node)
        else:
            break
    
    if isEven:
        print("YES")
    else:
        print("NO")


    