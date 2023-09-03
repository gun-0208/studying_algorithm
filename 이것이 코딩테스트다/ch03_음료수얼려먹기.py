# n x m 크기의 얼음 틀이 있을 때, 0은 구멍이 뚫려있는 부분, 1은 칸막이로된 부분이다.
# 0이 인접한 곳 상하좌우는 모두 연결된 것으로 가정한다.
# 아이스크림을 만들 수 있는 개수?

# n * m 영역을 일단 모두 탐색을 하면서 방문한 곳은 기록하고, 방문한 곳이 0이라면 아이스크림 영역이므로, 그 인접한 부분을 모두 탐색해야한다.
# 그러면, 값이 0 이고, 방문한 적이 없는 노드를 찾아서 해당 영역에서 DFS를 실시하면 아이스크림 전체의 영역을 알 수 있을 것이다.
# 아이스크림 영역이 발견될 때 cnt += 1을 해준다.
def dfs(map_arr,i,j,visited):

    visited[i][j]=1
    # 현재위치에서 탐색가능한 방향: 상하좌우
    move_types = [[-1,0],[0,-1],[1,0],[0,1]]
    
    for move_type in move_types:
        # 상하좌우로 이동했을 때 영역을 벗어나면 무시
        next_i = i + move_type[0]
        next_j = j + move_type[1]
        if next_i < 0 or next_i >= n or next_j < 0 or next_j >=m:
            continue
        
        # 영역 안에 존재 and 해당위치의 값이 0 and 방문하지 않았다면 => 현재 이동한 방향으로 탐색 실시
        if visited[next_i][next_j] == 0 and map_arr[next_i][next_j] == 0:

            dfs(map_arr,next_i,next_j,visited)


n,m = map(int,input().split())

visited = [[0] * m for _ in range(n)]

map_arr = []
for _ in range(n):
    map_arr.append(list(map(int,input().split())))

cnt = 0
for i in range(len(map_arr)):
    for j in range(len(map_arr[i])):

        # 방문하지 않았고, 현재 노드가 0으로 뚫려있는 경우 dfs 탐색 실시
        if map_arr[i][j] == 0 and visited[i][j] == 0:
            print(f"x={i}, y={j} 에서 DFS 시작:")
            cnt += 1
            dfs(map_arr,i,j,visited)

print(cnt)
