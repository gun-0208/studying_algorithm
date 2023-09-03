import sys
MOD = 1000000007
input = sys.stdin.readline

n,m,k = map(int,input().split())

tree_height = 0
length = n
while length > 0:
    length //= 2
    tree_height += 1

tree_size = pow(2,tree_height+1)
tree = [1] * tree_size

start_node_index = pow(2,tree_height)
for i in range(start_node_index, start_node_index+n):
    tree[i] = int(input())

index = tree_size - 1
while index > 1:
    tree[index//2] *= (tree[index] % MOD)
    index -= 1

def update(index,value):
    index = index + start_node_index - 1
    tree[index] = value

    while index > 1:
        index //= 2
        tree[index] = (tree[2 * index] % MOD) * (tree[2 * index + 1] % MOD)

def get_multi(start,end):
    start = start + start_node_index - 1
    end = end + start_node_index - 1

    part_multi = 1
    while start <= end:
        if start % 2 == 1:
            part_multi *= tree[start] % MOD
            start += 1
        if end % 2 == 0:
            part_multi *= tree[end] % MOD
            end -= 1
        start //= 2
        end //= 2
        part_multi %= MOD
    return part_multi

for _ in range(m+k):
    q,s,e = map(int,input().split())

    if q == 1:
        update(s,e)
    elif q == 2:
        print(get_multi(s,e))
