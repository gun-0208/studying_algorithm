n = int(input())

start_index = end_index = 1
summation = 1
cnt = 1

while end_index != n:
    if summation == n:
        cnt += 1
        end_index += 1
        summation += end_index
    elif summation > n:
        summation -= start_index
        start_index += 1
    else:
        end_index += 1
        summation += end_index

print(cnt)