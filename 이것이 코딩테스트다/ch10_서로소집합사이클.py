def get_parent(parent_list, x):
    if parent_list[x] != x:
        parent_list[x] = get_parent(parent_list,parent_list[x])
    
    return parent_list[x]

def union_parent(parent_list,a,b):
    a_root = get_parent(parent_list,a)
    b_root = get_parent(parent_list,b)

    if a_root > b_root:
        parent_list[a] = b_root
    else:
        parent_list[b] = a_root

v,e = map(int,input().split())
cycle = False

parent_list = [i for i in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    
    if get_parent[a] == get_parent[b]:
        cycle=True
        break

    else:
        union_parent(parent_list,a,b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 x")


