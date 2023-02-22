from collections import deque
cnt = 0 # 내구도가 0인 칸 갯수
i = 0 # 현재 "올리는 위치"인 칸
robots = [0] # 현재 로봇들의 위치 리스트

def first(i, robots):
    for robot in robots:
        robot += 1
    i += 1
    return i, robots

def second(robots):
    for robot in robots:
        next = (robot+1) % N
        if A[next] != 0 and not robots[next]:  # 내구도가 0이 아니고 로봇이 없다면
            robot += 1
        elif A[next] == 0:
            cnt += 1
    if cnt == K:
        return -1
    else:
        return robots

def third(i, robots):
    if A[i] != 0:
        robots.append(i)
    return i, robots

def fourth():
    

N,K = map(int,input().split())
A = list(map(int,input().split()))
while cnt < K:
    if A[i] != 0:   # 올리는 칸이 내구도가 남아있으면 로봇 올리기
        A[i] -= 1
        robots.append(i)
    else:  # 내구도가 0이라면 cnt += 1
        cnt += 1
    new_robots = []
    while robots:
        robot = robots.popleft()
        if A[(robot + 1) % N] != 0:
            new_robots.append((robot+1)%N)
        else: