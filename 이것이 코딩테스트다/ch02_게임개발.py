''' 캐릭터가 있는 장소는 1x1크기의 정사각형으로 이뤄진 n * m 크기의 직사각형.
각각의 칸은 육지 혹은 바다이다.
캐릭터가 동서남북 방향으로 갈 수 있을 때, 바다로 된 공간은 갈 수 없다.
1. 현재위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽방향으로 회전한 다음 왼쪽으로 한칸전진 
    왼쪽에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 가본 칸이거나 바다로 되어 있는 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간ㄷ.
이때, 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
- 0 : 북쪽
- 1 : 동쪽
- 2 : 남쪽
- 3 : 서쪽
'''

# 맵 크기 n * m 입력
n, m = map(int,input().split())

# 현재 row,col, direction 입력
row, col, direction = map(int,input().split())

# 방문한 곳 기록할 배열 선언[시작위치는 캐릭터가 방문했으므로 1로 바꿈.]
visited = [[0] * m for _ in range(n)]
visited[row][col] = 1

# 게임 맵 배열 입력받기
map_arr = []
for _ in range(n):
    map_arr.append(list(map(int,input().split())))

# 방향 벡터 딕셔너리 형태로 선언
move_types = {0:[-1,0],1:[0,-1],2:[1,0],3:[0,1]}

cnt = 1
turn_time = 0

# 탐색시작
while True:
    # turn left
    direction -= 1
    if direction == -1:
        direction = 3

    # 현재 위치에서 현재 방향으로 step 이동 [확정이 아니므로 next_row,next_col에 저장]
    next_row = row + move_types[direction][0]
    next_col = col + move_types[direction][1]

    # 이동한 위치가 육지이고, 방문한 적이 없다면 해당 방향으로 이동 확정
    if map_arr[next_row][next_col] == 0 and visited[next_row][next_col] == 0:
        row = next_row
        col = next_col
        visited[row][col] = 1
        cnt += 1
        turn_time = 0

    # 이동할 위치가 바다이거나, 방문한 적이 있다면 갈 수 없으므로 방향 변경 turn_time += 1
    # 올바른 곳으로 이동할 때 까지 해당 조건문 반복
    else:
        turn_time += 1
    
    # 그러다 turn_time == 4[네 방향으로 모두 돌았는데 갈 곳이 없는 경우]
    if turn_time == 4:
        # 뒤로 빼야하는데, 아직 확정되지 않음.
        next_row = row - move_types[direction][0]
        next_col = col - move_types[direction][1]

        # 뒤로 빼는데 맵이 바다가 아니라면 row,col 확정
        if map_arr[next_row][next_col] == 0:
            row = next_row
            col = next_col
        # 뒤로 빼는데 바다라면 탐색 끝.
        else:
            break
        # 뒤로 빼는데 성공했다면 turn_time 초기화.[해당 위치에서 들를 방향을 다시 찾아야 됨.]
        turn_time = 0

print(cnt)






