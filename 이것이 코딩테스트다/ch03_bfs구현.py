from collections import deque

def bfs(graph, node, visited):
    visited[node] = 1
    queue = deque([node])

    while queue:
        curr_node = queue.popleft()
        print(curr_node, end = ' ')

        for i in graph[curr_node]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
            


graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [0] * len(graph)

bfs(graph,1,visited)