from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int,input().split()))
    node = data[0]
    connected = data[1:-1]
    
    for i in range(0,len(connected)-1,2):
        graph[node].append((connected[i],connected[i+1]))
    
def BFS(node):
    visited[node] = [0,1]
    q = deque()
    q.append((node,0))

    while q:
        curr_node,curr_dist = q.popleft()

        for next_node, next_dist in graph[curr_node]:
            if visited[next_node][1] == 0:
                q.append((next_node,next_dist))
                visited[next_node] = [visited[curr_node][0] + next_dist,1]
visited = [[0] * 2 for _ in range(n+1)]
BFS(1)

Max = 0
max_idx = 0

for i in range(1,n+1):
    if Max < visited[i][0]:
        Max = visited[i][0]
        max_idx = i

visited = [[0] * 2 for _ in range(n+1)]
BFS(max_idx)

print(max(visited)[0])

