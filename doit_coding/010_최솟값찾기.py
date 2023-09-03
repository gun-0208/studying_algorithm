import sys
from collections import deque

input = sys.stdin.readline

n,l = map(int,input().split())
array = list(map(int,input().split()))
q = deque()

for i in range(n):
    while q and q[-1][0] > array[i]:
        q.pop()

    q.append((array[i],i))

    if q[0][1] <= i - l:
        q.popleft()
    print(q[0][0], end=" ")

