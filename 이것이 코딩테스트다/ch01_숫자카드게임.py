n, m = map(int,input().split())

num_array = [list(map(int,input().split())) for _ in range(n)]

max_result = 0

for row in num_array:
    min = 10001
    for col in row:
        if col < min:
            min = col
    if min > max_result:
        max_result = min

print(max_result)    
