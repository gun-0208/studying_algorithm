import sys
input = sys.stdin.readline

n = int(input())

def check(number):
    for i in range(2,int(number/2 + 1)):
        if number % i == 0:
            return False
    return True

def DFS(number):
    if len(str(number)) == n:
        print(number)
        return

    else:
        for i in range(1,10,2):
            if check(number * 10 + i):
                DFS(number*10 + i)
    
for i in [2,3,5,7]:
    DFS(i)