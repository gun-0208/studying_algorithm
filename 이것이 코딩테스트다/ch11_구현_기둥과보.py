# n : 설치영역
# build_frame : [[x,y,stuff,job],...] => (x,y): 설치좌표, stuff:0=> 기둥, 1=> 보, job:0=>삭제,1=>설치
# 기둥은 좌표가 바닥(y=0)이거나, 아래가 기둥일 경우(x,y-1,0), 왼쪽이 보일 경우(x-1,y,1) 오른쪽이 보일경우(x+1,y,1) 설치 가능하다.
# 보는 왼쪽 아래가 기둥일 경우(x,y-1,0) 오른쪽 아래가 기둥일 경우(x+1,y-1,0), 양끝이 보일경우(x-1,y,1)and(x+1,y,1) 설치 가능하다.
# 일단 설치나 삭제를 해보고 저장되어 있는 빌드 리스트를 순회하면서 빌드 조건에 문제가 없는지 체크하는 방향으로 구성한다.
 
def solution(n,build_frame):
    answer = []

    for frame in build_frame:
        x,y,stuff,job = frame

        if job == 1: # 설치하는 경우
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])

        else:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])

    return sorted(answer)


def possible(answer):
    
    for x,y,stuff in answer:

        if stuff == 0: # stuff가 기둥인 경우
            if y == 0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            return False

        elif stuff == 1: # stuff가 보인 경우
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
        
    return True
