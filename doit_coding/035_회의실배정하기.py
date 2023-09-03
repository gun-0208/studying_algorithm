from queue import PriorityQueue

n = int(input())
q = PriorityQueue()

for _ in range(n):
    s ,e = map(int,input().split())

    q.put((e,s))

curr_time = -1
cnt = 0

while q.qsize() > 0:
    end,start = q.get()

    if start >= curr_time:
        curr_time = end
        cnt += 1

print(cnt)