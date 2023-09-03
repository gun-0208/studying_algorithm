from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
cost = [0] * (n+1)
indegree = [0] * (n+1)

for i in range(1,n+1):
    data = list(map(int,input().split()))[:-1]
    cost[i] += data[0]
    del data[0]

    for j in data:
        graph[j].append(i)
        indegree[i] += 1

q = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

result = [0] * (n+1)

while q:
    node = q.popleft()

    for next in graph[node]:
        indegree[next] -= 1
        
        result[next] = max(result[next],result[node] + cost[node])

        if indegree[next] == 0:
            q.append(next)

for i in range(1,n+1):
    print(result[i] + cost[i])
        
