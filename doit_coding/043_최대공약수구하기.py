def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

len_A, len_B = map(int,input().split())

len_gcd = gcd(len_A,len_B)

answer = ""

for _ in range(len_gcd):
    print(1,end="")