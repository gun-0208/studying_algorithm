
# def calc_chicken_dist(home_list,chicken_list):
#     for i, home in enumerate(home_list):
#         x1, y1, x2,y2 = home

#         if x2 == 9999 and y2 == 9999:
#             distance = 9999
#             min_chicken_idx = 9999
#             min_cnt = 9999

#             for j, chicken in enumerate(chicken_list):
#                 cnt, x2,y2 = chicken
#                 temp_dist = abs(x1-x2) + abs(y1-y2)
#                 if distance > temp_dist:
#                     distance = temp_dist
#                     min_chicken_idx = j
#                     min_cnt = cnt

#             chicken_list[min_chicken_idx][0] = min_cnt + 1
#             home_list[i][2:] = chicken_list[min_chicken_idx][1:]

#     return sorted(chicken_list), home_list

# n,m = map(int,input().split())

# array= [[0] * (n+1) for _ in range(n+1)]

# chicken_list = []
# home_list = []

# for i in range(1,n+1):
#     input_list = list(map(int,input().split()))
    
#     for j in range(1,n+1):
#         array[i][j] = input_list[j-1]
#         if input_list[j-1] == 1:
#             home_list.append([i,j,9999,9999])
#         elif input_list[j-1] == 2:
#             chicken_list.append([0,i,j])

# while True:
#     chicken_list, home_list = calc_chicken_dist(home_list,chicken_list)
#     print(home_list)

#     if len(chicken_list) == m:
#         break

#     cnt,x2,y2 = chicken_list.pop(0)


#     for idx in range(len(home_list)):
#         if home_list[idx][2:] == [x2,y2]:
#             home_list[idx][2:] = [9999,9999]

# total_distance = 0
# for home in home_list:
#     x1,y1,x2,y2 = home

#     total_distance += (abs(x1-x2) + abs(y1-y2))


# print(chicken_list)
# print(home_list)

# print(total_distance)

# 치킨집 중에서 M개를 고르는 조합을 생각해보자.
from itertools import combinations

n,m = map(int,input().split())
chicken, house = [], []

for row in range(n):
    data = list(map(int,input().split()))
    
    for col in range(n):
        if data[col] == 1:
            house.append((row,col))

        elif data[col] == 2:
            chicken.append((row,col))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken,m))

print(candidates)

def get_sum(candidate):
    result = 0

    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp,abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

result = 1e9

for candidate in candidates:
    result = min(result,get_sum(candidate))

print(result)        