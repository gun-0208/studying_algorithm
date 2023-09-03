# N개의 부품을 가지고 있다. 각 부품에는 구분할 수 있는 고유번호가 써져있다.
# 외부에서 M개 종류의 부품을 구매한다고 할 때, 해당 부품이 있다면 yes , 없다면 No를 출력하도록 한다.
# 1 <= n,m <= 1,000,000
# n개의 부품이 정렬이 안된 상태로 존재하므로, 이를 일단 라이브러리를 이용해 정렬 한뒤, M개의 부품이 입력된 리스트에서 하나씩 뽑아서
# n개의 부품이 있는 리스트에서 이진탐색으로 찾아보면 될 것이다. 이럴 경우 최악의 시간복잡도는 O(m * nlogn)이다.

# n,m의 범위가 정해져있으므로 계수정렬도 이용가능하다.

count_arr = [0] * 1000001

n = int(input())
array = list(map(int,input().split()))

for i in array:
    count_arr[i] += 1

m = int(input())

targets = list(map(int,input().split()))

for target in targets:
    if count_arr[target] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")