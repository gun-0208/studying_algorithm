import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

nodes = [i for i in range(n+1)]

def find(a):
    if a == nodes[a]:
        return a
    else:
        nodes[a] = find(nodes[a])
        return nodes[a]
    
def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        nodes[b] = a
    
def check(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return True
    return False

for _ in range(m):
    data = list(map(int,input().split()))

    if data[0] == 0:
        union(data[1],data[2])
    elif data[0] == 1:
        isGroup = check(data[1],data[2])

        if isGroup:
            print("YES")
        else:
            print("NO")