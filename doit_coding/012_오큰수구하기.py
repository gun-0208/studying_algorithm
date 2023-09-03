import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
answer = [0] * n
myStack = []

for i in range(n):
    while myStack and array[myStack[-1]] < array[i]:
        index = myStack.pop()
        answer[index] = array[i]
    myStack.append((i))

while myStack:
    index = myStack.pop()
    answer[index] = -1

result = ""

for i in range(n):
    sys.stdout.write(str(answer[i])+" ")

print(result)