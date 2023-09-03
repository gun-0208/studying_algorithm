import sys
input = sys.stdin.readline

n,m = map(int,input().split())

edges = []
for _ in range(m):
    s,e,w = map(int,input().split())
    edges.append((s,e,w))

distance = [1e9] * (n+1)
distance[1] = 0

for _ in range(n-1):
    for start,end,weight in edges:
        if distance[start] != 1e9 and distance[end] > distance[start] + weight:
            distance[end] = distance[start] + weight

isCycle = False
for start, end, weight in edges:
    if distance[start] != 1e9 and distance[end] > distance[start] + weight:
        isCycle = True

if isCycle:
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] != 1e9:
            print(distance[i])
        else:
            print(-1)

