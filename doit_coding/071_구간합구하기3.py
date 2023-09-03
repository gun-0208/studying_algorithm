import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

leaf_size = n
tree_height = 0
while leaf_size != 0:
    leaf_size //= 2
    tree_height += 1

tree_size = pow(2,tree_height + 1)
leaf_start_index = tree_size//2 - 1

tree = [0] * tree_size
for i in range(leaf_start_index+1,leaf_start_index+n+1):
    tree[i] = int(input())

def set_tree(i):
    while i != 1:
        tree[i//2] += tree[i]
        i -= 1

set_tree(tree_size-1)

def change_val(index,value):
    diff = value - tree[index]

    while index > 0:
        tree[index] += diff
        index //= 2

def get_sum(s,e):
    part_sum = 0
    while s <= e:
        if s % 2 == 1:
            part_sum += tree[s]
            s += 1
        if e % 2 == 0:
            part_sum += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return part_sum

for _ in range(m+k):
    question, s,e = map(int,input().split())

    if question == 1:
        change_val(leaf_start_index+s,e)
    elif question == 2:
        part_sum = get_sum(leaf_start_index+s,leaf_start_index+e)
        print(part_sum)
