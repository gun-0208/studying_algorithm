# 절단기의 높이 H를 지정하여 떡을 자른다.
# 떡은 모두 길이가 다른 N개의 떡이 주어진다.
# 떡은 H를 넘는 길이의 떡만 잘릴 것이다. 잘린 떡의 높이 합만큼 손놈이 가져간다고 할 때, 길이 최소 M만큼의 떡을  얻어가기 위해 
# 자를 수 있는 H의 최댓값?

# 떡의 길이가 모두 다르고, H값을 조정해가면서 M을 구해가야 한다. 값의 범위가 매우 크므로, H값을 선정할 때, 순차적으로 접근하면 시간초과가 날 것이다.
# 이진 탐색을 통해 h를 조정하면서 M이 될 때까지 탐색해보자.

n,m = list(map(int,input().split(' ')))
array = list(map(int,input().split()))

# 떡의 최대 높이를 end로 두고 해당 범위 안에서 적정 값 h를 이진탐색으로 찾을 것이다.
start = 0
end = max(array)

result = 0
while start <= end:
    mid = (start + end) // 2

    sum_temp = 0
    for arr in array:
        if arr - mid >= 0:
            sum_temp += (arr - mid)
    
    # 자른 떡의 합이 m보다 큰 경우 높이를 좀더 크게해줄 수 있으므로, 범위를 오른쪽으로 변경
    if sum_temp > m:
        result = mid # 최대한 덜 잘랐을 떄가 정답이므로, 이때도 기록
        start = mid + 1
    # 자른 떡의 합이 m보다 작은 경우 높이를 좀더 작게해줄 수 있으므로, 범위를 왼쪽으로 변경
    elif sum_temp < m:
        end = mid -1
    else:
        result = mid

print(result)

    