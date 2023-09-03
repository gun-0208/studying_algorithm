import sys

input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    array.append((int(input()), i))

sorted_array = sorted(array)
Max = 0
for i in range(n):
    if sorted_array[i][1] - i > Max:
        Max = sorted_array[i][1] - i

print(Max+1)