import math

A,B = map(int,input().split())
array = [0] * (B+1)

for i in range(2,len(array)):
    array[i] = i

for i in range(2,int(math.sqrt(len(array))+1)):
    if array[i] == 0:
        continue
    for j in range(i+i, len(array),i):
        array[j] = 0

count = 0

for i in range(2,B+1):
    if array[i] != 0:
        temp = array[i]

        while array[i] <= B/temp:
            if array[i] >= A/temp:
                count += 1
            temp = temp * array[i]
print(count)