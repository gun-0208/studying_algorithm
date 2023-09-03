n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

result = True
index = 1
answer = ""
myStack = []

for i in range(n):
    if array[i] >= index:
        while array[i] >= index:
            myStack.append(index)
            index += 1
            answer += "+\n"
        myStack.pop()
        answer += "-\n"
    
    else:
        popped = myStack.pop()
        if popped > array[i]:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result == True:
    print(answer)