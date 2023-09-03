from queue import PriorityQueue

n = int(input())
plus_q = PriorityQueue()
minus_q = PriorityQueue()
zero_cnt = 0
one_cnt = 0

for _ in range(n):
    data = int(input())
    
    if data > 1:
        plus_q.put(data * (-1))
    elif data == 1:
        one_cnt += 1
    elif data == 0:
        zero_cnt += 1
    elif data < 0:
        minus_q.put(data)

summation = 0

while plus_q.qsize() > 1:
    num1 = plus_q.get() * (-1)
    num2 = plus_q.get() * (-1)

    summation += num1 * num2

if plus_q.qsize() > 0:
    summation += plus_q.get() * (-1)

while minus_q.qsize() > 1:
    num1 = minus_q.get()
    num2 = minus_q.get()

    summation += num1 * num2

if minus_q.qsize() > 0:
    if zero_cnt == 0:
        summation += minus_q.get()

summation += one_cnt

print(summation)

