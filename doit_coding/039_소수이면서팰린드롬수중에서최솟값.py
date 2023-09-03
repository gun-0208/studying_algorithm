import math

n = int(input())
array = [0] * 10000001

for i in range(2,len(array)):
    array[i] = i

for i in range(2,int(math.sqrt(len(array))+1)):
    if array[i] == 0:
        continue

    for j in range(i+i, len(array), i):
        array[j] = 0

result = 0

for i in range(n,len(array)):
    if array[i] == 0:
        continue
    value = str(array[i])
    value_reverse = value[::-1]

    if value == value_reverse:
        result = array[i]
        break

print(result)