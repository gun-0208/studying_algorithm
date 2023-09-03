# 정수 n이 입력되면 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의수
# 시각(h)은 0 ~ 12시 사이의 값
# 분(m)은 0 ~ 60분 사이의 값
# 초(s)는 0 ~ 60초 사이의 값
n = int(input())

cnt = 0
for h in range(0,n+1):
    for m in range(0,60):
        for s in range(0,60):
            curr_time = "{:02d}:{:02d}:{:02d}".format(h,m,s)
            if "3" in curr_time:
                print(curr_time)
                cnt += 1


print(cnt)
