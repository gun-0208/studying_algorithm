from itertools import combinations

def virus(row,col):
    for move in move_types:
        nrow = row + move[0]
        ncol = col + move[1]

        if nrow >= 1 and nrow <= n and ncol >= 1 and ncol <= m:
            if temp[nrow][ncol] == 0:
                temp[nrow][ncol] = 2
                virus(nrow,ncol)

n,m = map(int,input().split())
array = [[-1] * (m+1) for _ in range(n+1)]
space_list = []
move_types = [(0,1),(1,0),(0,-1),(-1,0)]
result = 0

for i in range(1,n+1):
    input_data = list(map(int,input().split()))
    for j in range(1,m+1):
        array[i][j] = input_data[j-1]
        
        if array[i][j] == 0:
            space_list.append((i,j))

temp = [[-1] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        temp[i][j] = array[i][j]
candidates = list(combinations(space_list,3))

for candidate in candidates:
    for row,col in candidate:
        # print(candidate)
        temp[row][col] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if temp[i][j] == 2:
                virus(i,j)
    
    score = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if temp[i][j] == 0:
                score += 1
    
    result = max(result,score)
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            temp[i][j] = array[i][j]
            
print(result)    
