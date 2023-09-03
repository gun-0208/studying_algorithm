import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
m = int(input())

nodes = [i for i in range(n+1)]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        nodes[a] = b

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

for i in range(1,n+1):
    data = [0] + list(map(int,input().split()))

    for j in range(1,n+1):
        if data[j] == 1:
            union(j,i)

plans = list(map(int,input().split()))

for plan in plans:
    isGroup = check(plan,plans[0])

    if isGroup == False:
        break

if isGroup:
    print("YES")
else:
    print("NO")