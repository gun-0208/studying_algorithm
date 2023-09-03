from collections import deque

inits = list(map(int,input().split()))
visited = [[False] * 201 for _ in range(201)]
answer = []

change_types = [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]

def BFS():
    visited[0][0] = True
    answer.append(inits[2])
    
    q = deque()
    q.append((0,0))

    while q:
        curr_a, curr_b = q.popleft()
        curr_c = inits[2] - curr_a - curr_b

        for send, receive in change_types:
            next = [curr_a,curr_b,curr_c]

            next[receive] += next[send]
            next[send] = 0

            if next[receive] > inits[receive]:
                next[send] = next[receive] - inits[receive]
                next[receive] = inits[receive]

            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                q.append((next[0],next[1]))

                if next[0] == 0:
                    answer.append(next[2])

BFS()
answer.sort()

for i in answer:
    print(i,end=" ")    