from collections import deque

v,e = map(int,input().split())

graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)

for _ in range(e):
    a,b = map(int,input().split())

    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    q = deque()

    for idx in range(1,len(indegree)):
        if indegree[idx] == 0:
            q.append((idx,graph[idx]))

    while q:
        curr_node, next_nodes = q.popleft()
        print(curr_node, end = ' ')

        for next in next_nodes:
            indegree[next] -= 1
            
            if indegree[next] == 0:
                q.append((next,graph[next]))

topology_sort()

