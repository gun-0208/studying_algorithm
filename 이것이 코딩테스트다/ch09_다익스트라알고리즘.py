import sys

input = sys.stdin.readline
INF = int(1e9) # 무한 => 10억

n,m =map(int,input().split())

# 시작점 설정
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n+1)]

# 방문한 적이 있는지 체크하는 리스트
visited = [False] * (n+1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선의 정보를 입력받기
for _ in range(m):
    # a번 노드 => b번 노드로 가는데 드는 비용이 c라는 의미
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단거리가 짧은 노드
    
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 거리 초기화
    distance[start] = 0
    visited[start] = True

    # 시작노드와 연결된 노드들을 하나씩 꺼내어 distance 바꿔줌.
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
        
