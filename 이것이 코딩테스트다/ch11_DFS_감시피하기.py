from itertools import combinations

move_types = [(0,1),(1,0),(0,-1),(-1,0)]

def DFS(i,j,move):
    # DFS 를 호출 했을 때, 매개변수로 받은 move 방향으로 종료조건 만날 때 까지 DFS 탐색
    global correct
    
    if i <= n and i >= 1 and j <= n and j >= 1:
        
        if temp[i][j] == "S":
            correct = False
            return correct
        elif temp[i][j] == "O":
            return correct
        i += move[0]
        j += move[1]

        DFS(i,j,move)
    return correct

n = int(input())

array = [[0] * (n+1) for _ in range(n+1)]

space_list = []

for i in range(1,n+1):
    data = input().split()
    for j in range(1,n+1):
        array[i][j] = data[j-1]
        
        if array[i][j] == "X":
            space_list.append((i,j))

candidates = list(combinations(space_list,3))

temp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        temp[i][j] = array[i][j]

        
for candidate in candidates:
    correct = True
    
    for row, col in candidate:
        temp[row][col] = 'O'

    for row in range(1,n+1):
        for col in range(1,n+1):
            if temp[row][col] == 'T':
                for move in move_types:
                    nrow = row + move[0]
                    ncol = col + move[1]

                    correct = DFS(nrow,ncol,move)

    if correct == True:
        print("YES")
        break

    for i in range(1,n+1):
        for j in range(1,n+1):
            temp[i][j] = array[i][j]

if correct == False:
    print("NO")




