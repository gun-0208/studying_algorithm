
def dfs(graph,node, visited):
    visited[node] = 1
    print(node, end = ' ')
    
    for i in graph[node]:
        if not visited[i]:
            dfs(graph,i,visited)


# 노드들을 dfs로 탐색하는 알고리즘을 만들어 보자.
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [0] * len(graph)

dfs(graph,1,visited)