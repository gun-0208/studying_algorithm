# 고정점이란, 수열의 원소중에서 그 값이 인덱스와 동일한 원소.
# a = {-15, -4, 2, 8, 13}이 있을떄, a[2]=2이므로, 고정점은 2
# 모든원소가 오름차순 정렬되어있음. 이 때, 고정점이 있다면 고정점 출력, 없으면 -1 출력
# 1<= n <= 1,000,000, -10^9 <= 각 원소의 값 <= 10^9
# 시간 복잡도 o(logN)넘으면 시간초과

n = int(input())
array = list(map(int,input().split()))

def binary_search(array,start,end):
    if start > end:
        return None
    
    mid = (start+end) // 2

    if array[mid] > mid:
        return binary_search(array,start,mid-1)
    elif array[mid] < mid:
        return binary_search(array,mid+1,end)
    else:
        return mid
    

index = binary_search(array,0,n-1)

if index == None:
    print(-1)
else:
    print(index)