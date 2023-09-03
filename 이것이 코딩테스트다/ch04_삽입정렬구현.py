array = [7,5,9,0,3,1,6,2,4,8]

# 특정 데이터 지점에서 왼쪽으로 출발하여 값을 비교함.
for i in range(1,len(array)):

    # i번째 데이터에서 왼쪽으로 한칸씩 이동하면서 값을 비교
    for j in range(i,0,-1):
        # 자신의 바로 왼쪽 데이터가 자신보다 크면 자리를 바꿔줌.
        # 왼쪽이 자신보다 작은 값이 올때 까지 왼쪽으로 계속 가면서 바꿔줌.
        if array[j] < array[j-1]:
            array[j-1],array[j] = array[j], array[j-1]
        else:
            # 왼쪽에 있는 값이 자신의 값보다 작은 경우, 이미 왼쪽은 정렬이 되어있는 상태이므로 바로 stop 
            break

print(array)