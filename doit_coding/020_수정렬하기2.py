# merge_sort를 이용한 오름차순 정렬
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
array = [0] * (n+1)
temp = [0] * (n+1)

for i in range(1,n+1):
    array[i] = int(input())

def merge_sort(start,end):
    if end - start < 1:
        return
    
    mid = (start+end) // 2

    merge_sort(start,mid)
    merge_sort(mid+1, end)

    for i in range(start,end+1):
        temp[i] = array[i]
    
    index1 = start
    index2 = mid+1
    k = start

    while index1 <= mid and index2 <= end:
        if temp[index1] > temp[index2]:
            array[k] = temp[index2]
            index2 += 1
            k += 1
        else:
            array[k] = temp[index1]
            index1 += 1
            k += 1
    
    while index1 <= mid:
        array[k] = temp[index1]
        index1 += 1
        k += 1
    while index2 <= end:
        array[k] = temp[index2]
        index2 += 1
        k += 1
    
merge_sort(1,n)

for i in range(1,n+1):
    print(str(array[i]) + '\n')