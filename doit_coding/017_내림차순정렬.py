import sys
print = sys.stdout.write

array = list(input())

for i in range(len(array)):
    Max = i
    for j in range(i+1,len(array)):
        if int(array[Max]) < int(array[j]):
            Max = j
    
    if int(array[i]) < int(array[Max]):
        temp = array[i]
        array[i] = array[Max]
        array[Max] = temp
        
for i in range(len(array)):
    print(array[i])