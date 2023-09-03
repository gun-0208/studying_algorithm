import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
nodes = [i for i in range(n+1)]

def find(a):
    if nodes[a] == a:
        return a
    else:    
        nodes[a] = find(nodes[a])
        return nodes[a]

def check(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return True
    return False

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        nodes[b] = a
    
truth = list(map(int,input().split()))
truth_num = truth[0]
del truth[0]

party = [[] for _ in range(m)]

for i in range(m):
    party[i] = list(map(int,input().split()))

    party_num = party[i][0]
    del party[i][0]

for i in range(m):
    first_person = party[i][0]

    for j in range(1,len(party[i])):
        union(first_person,party[i][j])

result = 0    
for i in range(m):
    is_possible = True
 
    for j in range(len(truth)):
        if check(party[i][0], truth[j]):
            is_possible = False
            break
    
    if is_possible:
        result += 1

print(result)
