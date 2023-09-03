# merge_sort를 이용해 버블정렬의 swap횟수 구하기
import sys
input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int,input().split()))
temp = [0] * (n+1)
swap_cnt = 0

def merge_sort(start,end):
    global array,temp,swap_cnt

    if end - start < 1:
        return
    
    mid = (start + end) // 2

    merge_sort(start,mid)
    merge_sort(mid+1,end)

    for i in range(start,end+1):
        temp[i] = array[i]
    
    index1 = start
    index2 = mid+1
    k = start

    while index1 <= mid and index2 <= end:
        if temp[index1] > temp[index2]:
            array[k] = temp[index2]
            k += 1
            index2 += 1
            swap_cnt += (index2 - k)
        else:
            array[k] = temp[index1]
            k += 1
            index1 += 1
    
    while index1 <= mid:
        array[k] = temp[index1]
        index1 += 1
        k += 1
    while index2 <= end:
        array[k] = temp[index2]
        index2 += 1
        k += 1

merge_sort(1,n)

print(swap_cnt)

