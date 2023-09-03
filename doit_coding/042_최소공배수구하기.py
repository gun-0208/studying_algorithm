def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

t = int(input())

for _ in range(t):
    A,B = map(int,input().split())

    print(int(A*B / gcd(A,B)))