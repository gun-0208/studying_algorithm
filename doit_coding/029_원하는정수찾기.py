def binary_search(start,end,target):
    global array, result

    if start > end:
        return 
    
    mid = (start + end) // 2

    if array[mid] == target:
        result = True
        return mid
    elif array[mid] > target:
        binary_search(start,mid-1,target)
    else:
        binary_search(mid+1,end,target)

n = int(input())
array = list(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))
array.sort()

for target in targets:
    result = False

    binary_search(0,n-1,target)

    if result == True:
        print(1)
    else:
        print(0)