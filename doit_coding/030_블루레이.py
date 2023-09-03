n,m = map(int,input().split())
array = list(map(int,input().split()))

start = max(array)
end = sum(array)

while start <= end:
    mid = (start + end) // 2

    temp_cnt = 0
    temp_size = 0

    for i in range(n):
        if temp_size + array[i] > mid:
            temp_cnt += 1
            temp_size = 0
        temp_size += array[i]
    
    if temp_size > 0:
        temp_cnt += 1

    if temp_cnt > m:
        start = mid + 1
    else:
        end = mid - 1    

print(start)