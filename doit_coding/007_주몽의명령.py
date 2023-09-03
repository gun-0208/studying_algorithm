import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
array = list(map(int,input().split()))

array.sort()

start = 0
end = n-1
cnt = 0

while start < end:
    temp_sum = array[start] + array[end]

    if temp_sum > m:
        end -= 1
    elif temp_sum < m:
        start += 1
    else:
        cnt += 1
        start += 1
        end -= 1

print(cnt)