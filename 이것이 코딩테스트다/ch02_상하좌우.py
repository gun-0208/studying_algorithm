# n*n 크기의 정사각형 공간 안에 (1,1)에서 출발하여 L,R,U,D 방향으로 한칸씩 이동한다고 할 때 최종 도착좌표는?
# 맵을 벗어나는 방향키의 경우 무시됨.
n = int(input())
input_vectors = list(input().split())

vector_dict = {'L':[0,-1],'R':[0,1],'U':[-1,0],'D':[1,0]}

row = 1
col = 1

for vector in input_vectors:
    row += vector_dict[vector][0]
    col += vector_dict[vector][1]

    if row > n or row < 1 or col > n or col < 1:
        row -= vector_dict[vector][0]
        col -= vector_dict[vector][1] 

print(f'{row} {col}')