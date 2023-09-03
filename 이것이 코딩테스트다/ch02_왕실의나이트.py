# 체스 판은 8 x 8 좌표 평면이다.
# 특정한 한칸에 나이트가 서 있을 때, 이동할 때 L자 형태로만 이동가능하다. 정원 밖으로는 나갈 수 없다.
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한칸 이동하기
# 2. 수직으로 두칸 이동한 뒤에 수평으로 한칸 이동하기

init_pos = input()
row = int(init_pos[1])
col = int(ord(init_pos[0])) - ord('a') + 1
vector_types = [(-2,-1),(-2,1),(-1,-2),(1,-2),(-1,2),(1,2),(2,-1),(2,1)]

cnt = 0
for vector in vector_types:
    next_row = row + vector[0]
    next_col = col + vector[1]

    if next_row > 8 or next_row < 1 or next_col > 8 or next_col < 1:
        continue

    cnt += 1

print(cnt)