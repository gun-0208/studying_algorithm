def get_parent(parent_list, x):
    if parent_list[x] != x:
        parent_list[x] = get_parent(parent_list,parent_list[x])

        return parent_list[x]
    
def union_parent(parent_list, a,b):
    a_root = get_parent(parent_list,a)
    b_root = get_parent(parent_list,b)

    if a_root < b_root:
        parent_list[b] = a_root
    else:
        parent_list[a] = b_root

v,e = map(int,input().split())

parent_list = [i for i in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    union_parent(parent_list, a,b)

# 부모테이블에서 루트노드만 출력
for i in range(1,len(parent_list)):
    print(parent_list[i], end= ' ')
print()


for i in range(1,len(parent_list)):
    get_parent(parent_list,i)