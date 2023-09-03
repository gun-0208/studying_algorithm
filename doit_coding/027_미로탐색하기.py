from collections import deque

n,m = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(input()))

visited = [[0] * m for _ in range(n)]
move_types = [(0,1),(1,0),(0,-1),(-1,0)]

def BFS():
    visited[0][0] = 1
    q = deque()
    q.append((0,0))

    while q:
        row,col = q.popleft()
        for move in move_types:
            next_row = row + move[0]
            next_col = col + move[1]

            if next_row >= 0 and next_row <= n-1 and next_col>=0 and next_col<=m-1:
                if int(array[next_row][next_col]) == 1 and visited[next_row][next_col] == 0:
                    q.append((next_row,next_col))
                    visited[next_row][next_col] = visited[row][col] + 1

BFS()
print(visited[n-1][m-1])