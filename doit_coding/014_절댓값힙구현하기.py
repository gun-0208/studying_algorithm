from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
q = PriorityQueue()

for i in range(n):
    data = int(input())

    if data == 0:
        if q.empty():
            print("0\n")
        else:
            temp = q.get()
            print(str((temp[1])) + "\n")
    else:
        q.put((abs(data),data))