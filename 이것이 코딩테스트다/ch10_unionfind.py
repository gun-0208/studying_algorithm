
def get_parent(parent_list,x):
    if parent_list[x] != x:
        return get_parent(parent_list,parent_list[x])
    
    return x


def union_parent(parent_list,a,b):
    a_root = get_parent(parent_list,a)
    b_root = get_parent(parent_list,b)

    if a_root > b_root:
        parent_list[a] = b_root
    else:
        parent_list[b] = a_root
    
v,e = map(int,input().split())

parent_list = [i for i in range(0,v+1)]

for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent_list,a,b)

print('각 원소가 속한 집합: ', end=' ')
for i in range(1,len(parent_list)):
    print(get_parent(parent_list,i), end=' ')

print()
print('부모 테이블: ' ,end=" ")
for i in range(1,len(parent_list)):
    print(parent_list[i], end=' ')