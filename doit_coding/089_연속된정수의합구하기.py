import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))

L = [0] * n
L[0] = array[0]

R = [0] * n
R[-1] = array[-1]

maximum = L[0]
for i in range(1,n):
    L[i] = max(array[i],L[i-1] + array[i])

    maximum = max(maximum, L[i])

for i in range(n-2,-1,-1):
    R[i] = max(array[i], R[i+1] + array[i])

for i in range(1,n-1):
    maximum = max(maximum, L[i-1] + R[i+1])

print(maximum)