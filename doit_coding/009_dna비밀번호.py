def add_alpha(alpha):
    global curr_list, targets, check_secret

    if alpha == 'A':
        curr_list[0] += 1
        if curr_list[0] == targets[0]:
            check_secret += 1
    elif alpha == 'C':
        curr_list[1] += 1
        if curr_list[1] == targets[1]:
            check_secret += 1
    elif alpha == 'G':
        curr_list[2] += 1
        if curr_list[2] == targets[2]:
            check_secret += 1
    elif alpha == 'T':
        curr_list[3] += 1
        if curr_list[3] == targets[3]:
            check_secret += 1

def sub_alpha(alpha):
    global curr_list, targets, check_secret

    if alpha == 'A':
        if curr_list[0] == targets[0]:
            check_secret -= 1
        curr_list[0] -= 1
    elif alpha == 'C':
        if curr_list[1] == targets[1]:
            check_secret -= 1
        curr_list[1] -= 1
    elif alpha == 'G':
        if curr_list[2] == targets[2]:
            check_secret -= 1
        curr_list[2] -= 1
    elif alpha == 'T':
        if curr_list[3] == targets[3]:
            check_secret -= 1
        curr_list[3] -= 1

curr_list = [0] * 4
check_secret = 0

n,m = map(int,input().split())
dna_str = list(input())
targets = list(map(int,input().split()))

answer = 0

for i in range(4):
    if targets[i] == 0:
        check_secret += 1

for i in range(m):
    add_alpha(dna_str[i])

if check_secret == 4:
    answer += 1

for end in range(m,n):
    start = end - m
    sub_alpha(dna_str[start])
    add_alpha(dna_str[end])

    if check_secret == 4:
        answer += 1

print(answer)
