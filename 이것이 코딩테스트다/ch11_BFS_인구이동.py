from collections import deque

n,l,r = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

move_types = [(0,1),(1,0),(0,-1),(-1,0)]
result = 0
total_count = 0

def process(row,col,index):
    united = []    
    united.append((row,col))

    q = deque()
    q.append((row,col))
    union[row][col] = index
    summary = graph[row][col]
    cnt = 1

    while q:
        row,col = q.popleft()

        for move in move_types:
            nrow = row + move[0]
            ncol = col + move[1]

            if nrow >= 0 and nrow < n and ncol >= 0 and ncol < n and union[nrow][ncol] == -1:
                diff = abs(graph[nrow][ncol] - graph[row][col])
                if diff >= l and diff <= r:
                    summary += graph[nrow][ncol]
                    cnt += 1
                    q.append((nrow,ncol))
                    united.append((nrow,ncol))

                    union[nrow][ncol] = index
        
    for i, j in united:
        graph[i][j] = summary // cnt
    return cnt

while True:
    union = [[-1] * (n) for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j,index)
                index += 1
    
    # index 가 n^2가 되었다는 것은 연합이 graph를 돌면서 하나도 이루어지지 않았다는 뜻.
    if index == n*n:
        break

    # index가 n*n이 아니라는 것은 연합이 형성된 곳은 union[i][j] != -1이기 때문에 거기서는 process()를 생략함. 따라서 index도 덜 증가함.
    # 연합 형성했으므로 전체 이동수 ++
    total_count += 1

print(total_count)




