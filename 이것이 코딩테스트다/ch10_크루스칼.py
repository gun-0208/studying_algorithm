def get_parent(parent, x):
    if parent[x] != x:
        parent[x] = get_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b):
    a_root = get_parent(parent,a)
    b_root = get_parent(parent,b)

    if a_root > b_root:
        parent[a] = b_root
    else:
        parent[b] = a_root
    
v,e = map(int,input().split())

parent = [i for i in range(v+1)]

edges = []

for _ in range(e):
    a,b,cost = map(int,input().split())

    edges.append((cost,a,b))

edges.sort()

result = 0
for edge in edges:
    cost,a,b = edge

    if get_parent(parent,a) != get_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)
    