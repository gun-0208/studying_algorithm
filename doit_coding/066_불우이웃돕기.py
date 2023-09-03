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
    
n = int(input())
array = [[0 for _ in range(n+1)] for _ in range(n+1)]

total = 0
for i in range(1,n+1):
    data = list(input())

    for j in range(1,n+1):
        alphabet = data[j-1]

        if alphabet == '0':
            array[i][j] = 0
        elif ord(alphabet) >= ord('a'):
            array[i][j] = ord(alphabet) - ord('a') + 1
        elif ord(alphabet) <= ord('Z'):
            array[i][j] = ord(alphabet) - ord('A') + 27
        
        total += array[i][j]

edges = PriorityQueue()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            continue
        if array[i][j] == 0:
            continue

        edges.put((array[i][j],i,j))

parent = [i for i in range(n+1)]
useEdge=0
while edges.qsize() > 0:
    weight, start, end = edges.get()

    if find(start) != find(end):
        union(start,end)
        useEdge += 1
        total -= weight

if useEdge == n-1:
    print(total)
else:
    print(-1)
