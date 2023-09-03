# 두개의 배열 A,B이 N개의 원소로 구성되어 있다. 원소는 모두 자연수
# k번 바꿔치기를 수행하는데, A에 있는 원소와 B에 있는 원소를 바꿔치기 한다.
# k번 바꿔치기 해서 배열 A의 모든 원소의 합이 최대가 되도록?

# => A 오름차순 정렬, B 내림차순 정렬하여 B의 최댓값과 A의 최솟값을 바꿔치기함. K번동안. range: 0 - k-1

# 퀵정렬 수행
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

def quick_sort_reverse(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x > pivot]
    right_side = [x for x in tail if x <= pivot]

    return quick_sort_reverse(left_side) + [pivot] + quick_sort_reverse(right_side)

n,k = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

B = quick_sort_reverse(B)
A = quick_sort(A)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else: 
        break
    
print(sum(A))