n = int(input())
array = list(map(int,input().split()))
s = [0] * n

for i in range(1,n):
    insert_point = i
    insert_value = array[i]

    for j in range(i-1,-1,-1):
        if array[i] > array[j]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = j

    for j in range(i,insert_point,-1):
        array[j] = array[j-1]
    
    array[insert_point] = insert_value

s[0] = array[0]

for i in range(1,n):
    s[i] = s[i-1] + array[i]

summation = 0

for i in range(n):
    summation += s[i]

print(summation)

