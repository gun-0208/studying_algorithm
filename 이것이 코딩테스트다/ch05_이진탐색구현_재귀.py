
# 배열이 정렬되어 있을 때, 해당 배열에서 target값의 위치를 알고 싶다.
# 이진탐색을 이용한다고 할 때 제일먼저 start,end가 input으로 주어지고, 그 중간값인 mid를 먼저 찾아야한다.
# 그 array[mid] 값이 target 값보다 크다면 해당 배열에서 mid 왼쪽 부분을 탐색하면되고, 작다면 오른쪽 부분을 탐색하면 된다.
# 해당 과정을 재귀함수를 이용해 끝까지 반복한다.
# 종료조건은 start 와 end 가 같아지거나 역전되는 시점, 또는 target == array[mid]일 경우 재귀함수를 종료한다.

def binary_search(array,target,start,end):
    mid = (start + end) // 2 # 중간값을 구할 때, 실수인 경우 버림.

    # start >= end인 경우 값을 못 찾았으므로 종료.
    if start > end:
        return None
    
    # 케이스 별로 나눠서 수행
    if array[mid] > target:
        # array[mid] > target인 경우 target은 mid의 왼쪽에 위치하므로 완쪽 구간으로 input값 변경.
        return binary_search(array,target,start,mid-1)

    elif array[mid] < target:
        # array[mid] < target인 경우 target은 mid의 오른쪽에 위치하므로 오른쪽 구간으로 Input값 변경.
        return binary_search(array,target,mid+1,end)
    else:
        # array[mid] == target이면 값을 찾았으므로 mid_index를 반환하고 탐색 종료
        return mid
    
n,target = map(int,input().split())
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)


