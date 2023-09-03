# n * m 크기의 직사각형 형태의 미로에 갇혀있다.
# 시작위치 (1,1), 출구는 (n,m)에 위치한다.
# 0은 지나갈 수 없고, 1로 된 곳만 지나갈 수 있다.
# (1,1) => (n,m) 까지 갈 때 움직인 최소 칸의 수?
from collections import deque
import numpy as np


def bfs(map_arr,row,col,visited):

    # 시작지점도 카운트에 포함.
    step_cnt = 1

    # BFS 수행할 큐 선언
    queue = deque()
    # 큐에 현재 위치 좌표와 현재까지 걸어온 카운트 대입 pop해서 현재 좌표와 카운트 값을 다음 스탭에 쓸 예정.
    queue.append((row,col,step_cnt))

    # 현재 위치에서 상하좌우로 조작 가능.
    move_types = [[-1,0],[0,-1],[1,0],[0,1]]

    # 큐가 빌 때 까지 반복 수행
    while queue:

        # 현재 위치와 카운트 pop해서 변수저장.
        curr_row, curr_col, step_cnt = queue.popleft()

        # 움직일 수 있는 방향이 총 4번이므로, 4번 동안 반복하면서 경우의 수 탐색
        for move_type in move_types:
            # 다음 스탭 임시로 저장
            next_row = curr_row + move_type[0] 
            next_col = curr_col + move_type[1]

            # 임시 저장된 다음 스탭이 영역을 벗어난다면 무시하고 다음 스탭 고려.
            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= m:
                continue

            # 다음 스탭을 했을 때, 해당 위치의 값이 1이고, 방문한 적이 없는 경우 다음 경로로 적당.
            if map_arr[next_row][next_col] == 1 and visited[next_row][next_col] == 0:

                # 다음 방문할 위치의 visited값에 1을 누적하여 카운트 값 할당
                visited[next_row][next_col] = step_cnt + 1

                # 다음 스탭 정보 큐에 추가
                queue.append((next_row,next_col, step_cnt+1))

# 맵크기 할당
n,m = map(int,input().split())

# 맵 정의
map_arr = []
for _ in range(n):
    map_arr.append(list(map(int,input().split())))

# 방문기록 표시할 배열 선언
visited = [[0] * (m) for _ in range(n)]

# 시작지점은 카운트에 포함하고 시작
visited[0][0] = 1

# 시작지점 부터 BFS로 해당위치에서 갈 수 있는 모든 곳을 체크 하면서 감.
bfs(map_arr,0,0,visited)

print(np.array(visited))

print("최종위치까지 간 경로의 수 : ",visited[n-1][m-1])