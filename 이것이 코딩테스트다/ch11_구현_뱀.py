
n = int(input())
k = int(input())

row = 1
col = 1
direction = 0
moves_curr_index = 0
time = 0
q = [(row,col)]



array = [[0] * (n+1) for _ in range(n+1)]
array[row][col] = 2

for _ in range(k):
    a_row, a_col = map(int,input().split())
    array[a_row][a_col] = 1

l = int(input())
moves = []
for _ in range(l):
    x,c = input().split()
    moves.append((int(x),c))

move_types = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}

while True:
    
    next_row = row + move_types[direction][0]
    next_col = col + move_types[direction][1]

    if next_row >= 1 and next_row <= n and next_col >= 1 and next_col <= n and array[next_row][next_col] != 2:

        if array[next_row][next_col] == 0:
            array[next_row][next_col] = 2
            q.append((next_row,next_col))
            q_row,q_col = q.pop(0)
            array[q_row][q_col] = 0
        
        if array[next_row][next_col] == 1:
            array[next_row][next_col] = 2
            q.append((next_row,next_col))
        

    else:

        time += 1
        break

    row = next_row
    col = next_col
    time += 1
    
    if moves_curr_index < l and time == moves[moves_curr_index][0]:
        
        if moves[moves_curr_index][1] == "L":
            direction -= 1
            if direction < 0:
                direction = 3
            
        else:
            direction += 1
            if direction > 3:
                direction = 0
        moves_curr_index += 1

print(time)