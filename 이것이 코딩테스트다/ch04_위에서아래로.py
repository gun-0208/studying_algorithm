# 크기에 상관없이 나열된 수들을 큰수부터 작은수의 순서로 정렬해야한다.
# 1 <= n <= 500
# 수의 범위 : 1 이상 100,000이하의 자연수

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

# 퀵정렬을 이용해보자.
# [15,27,12]가 들어온다면 어떻게 해야할까.

def quick_sort(array,start,end):
    # 먼저 start와 end가 역전된 경우 => array요소가 한개 이하라는 뜻
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left],array[right] = array[right], array[left]

    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)