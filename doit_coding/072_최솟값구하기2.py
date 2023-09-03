import sys
input = sys.stdin.readline

n,m = map(int,input().split())

tree_height = 0
length = n
while length > 0:
    length //= 2
    tree_height += 1

tree_size = pow(2,tree_height + 1)
start_node_index = pow(2,tree_height)

tree = [sys.maxsize] * tree_size
for i in range(start_node_index,start_node_index + n):
    tree[i] = int(input())

index = tree_size-1
while index > 1:
    tree[index//2] = min(tree[index//2], tree[index])
    index -= 1

def get_mini(start,end):
    start = start + start_node_index - 1
    end = end + start_node_index - 1
    
    part_mini = sys.maxsize
    while start <= end:
        if start % 2 == 1:
            part_mini = min(part_mini, tree[start])
            start += 1
        if end % 2 == 0:
            part_mini = min(part_mini, tree[end])
            end -= 1
        start //= 2
        end //= 2
    
    return part_mini

# print(tree)
for _ in range(m):
    s,e = map(int,input().split())
    print(get_mini(s,e))

        