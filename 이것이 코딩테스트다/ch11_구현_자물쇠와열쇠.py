# n * n 영역을 가진 key와 m * m 영역을 가진 lock
# key를 90도 돌리거나 lock 영역 안에서 이동 시키면서 lock을 풀려고 한다.
# lock은 해당 영역내 값이 key영역을 더해 모두 1이되면 열린다.
# 3 <= n,m <= 20, n <= m
# key는 lock의 영역 내 값을 모두 1로 만들기 위해 lock의 영역을 벗어나도 된다.

# lock의 영역을 3배로 키운 다음에, 슬라이딩 윈도우 방식으로 key를 하나씩 이동하면서 값을 연산하고, 해당 위치에서 lock영역이 모두 1이 되는지 확인하자.

def rotating_matrix_90_degree(array):
    row_len = len(array)
    col_len = len(array[0])

    rotated_array = [[0] * row_len for _ in range(col_len)]

    for i in range(row_len):
        for j in range(col_len):
            rotated_array[i][j] = array[j][row_len-1-i]
    
    return rotated_array
    
def check(new_lock):
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    
    return True

def solution(key,lock):
    lock_length = len(lock)
    key_length = len(key)

    new_lock = [[0] * (lock_length * 3) for _ in range(lock_length * 3)]

    for i in range(lock_length):
        for j in range(lock_length):
            new_lock[lock_length + i][lock_length + j] = lock[i][j]

    for rotation in range(4):
        key = rotating_matrix_90_degree(key)

        for row in range(lock_length * 2):
            for col in range(lock_length * 2):
                for i in range(key_length):
                    for j in range(key_length):
                        new_lock[row + i][col + j] += key[i][j]
                
                if check(new_lock) == True:
                    print(key)
                    return True
                
                for i in range(key_length):
                    for j in range(key_length):
                        new_lock[row+i][col+j] -= key[i][j]

    return False

                

print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))