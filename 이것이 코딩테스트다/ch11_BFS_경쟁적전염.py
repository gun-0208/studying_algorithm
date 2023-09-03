n,k = map(int,input().split())
array = [[-1] * (n+1) for _ in range(n+1)]
virus_q = []
temp_q = []

for i in range(1,n+1):
    data = list(map(int,input().split()))
    for j in range(1,n+1):
        array[i][j] = data[j-1]
        if array[i][j] != 0:
            virus_q.append((array[i][j], i, j))

s,x,y = map(int,input().split())

move_types = [(0,1),(1,0),(0,-1),(-1,0)]
time = 0

virus_q.sort()

while len(temp_q) > 0 or len(virus_q) > 0:
    while len(virus_q) > 0:
        virus_num, row, col = virus_q.pop(0)

        for move in move_types:
            nrow = row + move[0]
            ncol = col + move[1]

            if nrow >= 1 and nrow <= n and ncol >= 1 and ncol <= n:
                if array[nrow][ncol] == 0:
                    array[nrow][ncol] = virus_num
                    temp_q.append((virus_num,nrow,ncol))
    time += 1

    if time == s:
        print("s초 후 : ", array[x][y])
        
    while len(temp_q) > 0:
        virus_num, row, col = temp_q.pop(0)
        virus_q.append((virus_num,row,col))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(array[i][j], end=" ")
    print()

    
