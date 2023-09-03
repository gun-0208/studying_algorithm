import sys
input = sys.stdin.readline

n, k = map(int,input().split())
array = list(map(int,input().split()))

def quick_sort(start,end,k):
    global array
    if start < end:

        pivot = partition(start,end)

        if pivot > k:
            quick_sort(start,pivot-1,k)
        
        elif pivot < k:
            quick_sort(pivot+1,end,k)

        else:
            return


def partition(start,end):
    global array

    if start + 1 == end:
        if array[start] > array[end]:
            swap(start,end)
            return end
    
    mid = (start + end) // 2
    swap(start,mid)

    pivot = array[start]
    i = start + 1
    j = end

    while i <= j:
        while pivot < array[j] and j > 0:
            j -=1
        while pivot > array[i] and i < len(array) - 1:
            i += 1
        
        if i <= j:
            swap(i,j)
            i += 1
            j -= 1
        
    array[start] = array[j]
    array[j] = pivot

    return j

def swap(i,j):
    global array
    
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

quick_sort(0,n-1,k-1)

print(array[k-1])