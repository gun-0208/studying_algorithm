# 0과 1로만 이루어진 문자열 S.
# 이 문자열 s에 있는 모든 숫자를 전부 같게하려고 한다.
# s에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것.
#  s=0001100 일때,
# 1. 전체를 뒤집으면 1110011, 2. 4번째부터 5번째 까지 뒤집으면 1111111이 되어서 두번만에 모두 같은 숫자.
# but 처음부터 11을 뒤집으면 한번에 0000000이 되어서 1번만에 해결 가능. 최소 횟수?

s = input()

cnt0 = 0
cnt1 = 0
curr_group = 9999

for i in range(len(s)):
    curr_num = int(s[i])

    if curr_num != curr_group:
        if curr_num == 0:
            cnt0 += 1
        else:
            cnt1 += 1
        curr_group = curr_num

print(cnt0 if cnt0 < cnt1 else cnt1)