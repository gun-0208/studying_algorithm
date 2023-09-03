# 모험가 N명. 각 모험가마다 공포도가 숫자로 써있음.
# 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행 가능.
# 몇명의 모험가는 마을그대로에 남아있어도됨. 1 <= N <= 100,000. 최대한으로 짤 수 있는 그룹수?
# 2 3 1 2 2

n = int(input())

guild = list(map(int,input().split()))

guild.sort()

group = 0
cnt = 1

for i in range(len(guild)):
    guild[i] -= cnt

    if guild[i] <= 0:
        group += 1
        cnt = 1
    
    else:
        cnt += 1

print(guild)
print(group)

# 1 2 2 2 3 cnt = 1, group = 0
# 0 2 2 2 3 cnt = 1, group = 1
# 0 1 2 2 3 cnt = 2, group = 1
# 0 1 0 2 3 cnt = 1, group = 2
# 0 1 0 1 3 cnt = 2, group = 2
# 0 1 0 1 1 cnt = 3, group = 2
# 리스트에서 0이되거나 0보다 작은 수가 있는 위치에서 그룹이 형성된 것임.

