import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
array.sort()

answer = 0

for k in range(n):
    find = array[k]
    i = 0
    j = n-1

    while i<j:
        if array[i] + array[j] == find:
            if i != k and j != k:
                answer += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -=1
        elif array[i] + array[j] < find:
            i += 1
        else:
            j -= 1
print(answer)