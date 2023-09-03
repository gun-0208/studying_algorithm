import sys
from collections import deque
from queue import PriorityQueue
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# def DFS(row,col):
#     global island_num

#     visited[row][col] = True
#     array[row][col] = island_num

#     for move in move_types:
#         next_row = row + move[0]
#         next_col = col + move[1]

#         if next_row >= 0 and next_row < n and next_col >= 0 and next_col < m:
#             if not visited[next_row][next_col] and array[next_row][next_col] == 1:
#                 DFS(next_row,next_col)

def BFS(i,j):
    global island_num

    q = deque()
    q.append((i,j))
    visited[i][j] = True
    array[i][j] = island_num

    while q:
        row,col = q.popleft()
        for move in move_types:
            next_row = row + move[0]
            next_col = col + move[1]

            if next_row >= 0 and next_row < n and next_col >= 0 and next_col < m:
                if not visited[next_row][next_col] and array[next_row][next_col] == 1:
                    array[next_row][next_col] = island_num
                    visited[next_row][next_col] = True
                    q.append((next_row,next_col))
                    

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

n,m = map(int,input().split())

array = [[0 for _ in range(m)] for _ in range(n) ]

for i in range(n):
    array[i] = list(map(int,input().split()))

island_num = 1
visited = [[False] * (m) for _ in range(n)]

move_types = [(0,1),(1,0),(0,-1),(-1,0)]

for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            if not visited[i][j]:
                # DFS(i,j)
                BFS(i,j)
                island_num += 1

island_num -= 1
# print(array)

distance = [[sys.maxsize] * (island_num + 1) for _ in range(island_num + 1)]

for i in range(n):
    for j in range(m):
        if array[i][j] > 0:
            start_island = array[i][j]
            
            for move in move_types:
                next_row = i + move[0]
                next_col = j + move[1]

                steps = 0
                while next_row < n and next_row >= 0 and next_col >= 0 and next_col < m:
                    if array[next_row][next_col] == start_island:
                        break
                    elif array[next_row][next_col] == 0:
                        steps += 1

                    else:
                        if steps >= 2:
                            end_island = array[next_row][next_col]
                            distance[start_island][end_island] = min(distance[start_island][end_island],steps)
                            distance[end_island][start_island] = min(distance[end_island][start_island],steps)
                        steps = 0
                        break
                    next_row += move[0]
                    next_col += move[1]

edges = PriorityQueue()

for i in range(1,island_num+1):
    for j in range(1,island_num + 1):
        if distance[i][j] != sys.maxsize and distance[i][j] != 0:
            edges.put((distance[i][j],i,j))

parent = [i for i in range(island_num + 1)]

usedEdges = 0
summation = 0

while edges.qsize() > 0:
    weight, s, e = edges.get()
    
    if find(s) == find(e):
        continue

    union(s,e)
    usedEdges += 1
    summation += weight

if usedEdges == island_num - 1:    
    print(summation)    
else:
    print(-1)
        