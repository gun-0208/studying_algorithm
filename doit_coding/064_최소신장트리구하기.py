import sys
from queue import PriorityQueue
input = sys.stdin.readline

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

def check(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return True
    return False

V,E = map(int,input().split())
edges = PriorityQueue()

for _ in range(E):
    s,e,w = map(int,input().split())
    edges.put((w,s,e))

parent = [i for i in range(V+1)]

summation = 0
use_edge = 0

while use_edge < V-1:
    weight,start,end = edges.get()

    if check(start,end):
        continue
    
    union(start,end)
    summation += weight

    use_edge += 1

print(summation)


