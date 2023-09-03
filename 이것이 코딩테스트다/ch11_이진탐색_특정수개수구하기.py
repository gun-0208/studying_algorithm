# n개의 원소를 포함하고 있는 수열이 오름차순 정렬되어있다.
# {1,1,2,2,2,2,3}이 있을 때 2의 개수는 4개이다.
# 이 문제를 시간 복잡도 O(logN) 알고리즘으로 풀어야지만 시간 초과가 일어나지 않는다.

# 내 생각 : 복잡도를 줄이기 위해선 이진탐색 알고리즘을 이용해야 한다. 단, 특정 수가 특정 구간에서 연속적으로 나타날 수 있으므로 해당 수의 시작 부분과 끝 부분을 이진탐색으로 찾아야 한다. 특정 수는 순열에서 첫 부분, 또는 끝부분, 중간 부분에 위치해 있을 수 있으므로 탐색 조건을 잘 특정하자.

# 앞 부분의 숫자 탐색 : 특정 숫자의 앞부분은 index==0에 위치해 있거나, 해당 숫자의 index-=1 부분에 특정 숫자보다 작은수가 들어있을 것이다. 이 때는 특정 숫자의 앞부분을 찾은 것이므로 탐색을 종료한다.

# 뒷 부분의 숫자 탐색 : 특정 숫자의 뒷부분은 index==n-1에 위치해 있거나, 해당 숫자의 index+=1 부분에 특정 숫자보다 큰수가 들어있을 것이다. 이 대는 특정 숫자의 뒷부분을 찾은 것이므로 탐색을 종료한다.

# 오리지날 이진탐색 재귀함수 구현[이 알고리즘을 베이스로 first_search(), last_search()로 나눠서 구현하자.]
def binary_search(array,target,start,end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    
    else:
        return binary_search(array,target,mid+1,end)
    
def first_binary_search(array,target,start,end):
    if start > end:
        return None

    mid = (start+end) // 2

    if array[mid] == target and (mid == 0 or array[mid-1] < target):
        return mid
    
    elif array[mid] >= target:
        return first_binary_search(array,target,start,mid-1)
    
    elif array[mid] < target:
        return first_binary_search(array,target,mid+1,end)

def last_binary_search(array,target,start,end):
    if start > end:
        return None
    
    mid = (start+end) // 2

    if array[mid] == target and (mid == n-1 or array[mid+1] > target):
        return mid
    elif array[mid] > target:
        return last_binary_search(array,target,start,mid-1)
    elif array[mid] <= target:
        return last_binary_search(array,target,mid+1,end)
    
n,x = map(int,input().split())

array = list(map(int,input().split()))

start = first_binary_search(array,x,0,n-1)

end = last_binary_search(array,x,0,n-1)

if start is None:
    print(-1)
else:
    print(end-start+1)