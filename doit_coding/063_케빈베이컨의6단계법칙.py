import sys
input = sys.stdin.readline

n,m = map(int,input().split())

array = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    array[i][i] = 0

for _ in range(m):
    s,e = map(int,input().split())

    array[s][e] = 1
    array[e][s] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            array[i][j] = min(array[i][j], array[i][k] + array[k][j])

minimum = sys.maxsize
min_i = -1

for i in range(1,n+1):
    temp_sum = 0
    for j in range(1,n+1):
        temp_sum += array[i][j]
    
    if temp_sum < minimum:
        minimum = temp_sum
        min_i = i

print(min_i)