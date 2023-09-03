n_str = input()

right_start = len(n_str) // 2

left_sum = 0
right_sum = 0

for i in range(right_start,len(n_str)):
    right_sum += int(n_str[i])
    left_sum += int(n_str[::-1][i])


print("LUCKY" if left_sum == right_sum else "READY")