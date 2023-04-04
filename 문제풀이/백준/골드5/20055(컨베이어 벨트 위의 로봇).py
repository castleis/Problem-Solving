N,K = map(int,input().split())
durability = list(map(int,input().split()))
robot_pos = []             # 현재 로봇이 위치해있는 컨베이어 벨트의 인덱스들을 담아둘 리스트
is_robot = [False]*N
up_pos, down_pos = 0, N-1  # 올리는 위치, 내리는 위치. 벨트가 회전할 때마다 *_pos - 1

def robot_moving():
    global robot_pos
    new_robot_pos = []
    for r_pos in robot_pos:
        n_pos = r_pos + 1
        if is_robot[n_pos] or durability[n_pos] < 1:
            new_robot_pos.append(r_pos)
        else:   # 다음 위치에 로봇이 없고 내구도가 남아 있을 때만 이동
            durability[n_pos] -= 1              # 다음 위치의 내구도 -1
            is_robot[r_pos] = False
            if n_pos != down_pos:
                new_robot_pos.append(n_pos)     # new_robot_pos에 다음 위치 추가
                is_robot[n_pos] = True
    robot_pos = new_robot_pos
    return

def up_robot():
    if durability[up_pos] > 0:                  # 올리는 위치의 내구도가 0이 아닐 때
        robot_pos.append(up_pos)                    # robot_pos에 로봇 올리기
        is_robot[up_pos] = True
        durability[up_pos] -= 1
    return

def rotate():
    global robot_pos, is_robot

    d = durability.pop()
    durability.insert(0,d)

    new_robot_pos = []
    is_robot = [False]*N
    for r_pos in robot_pos:
        if r_pos+1 < down_pos:
            is_robot[r_pos], is_robot[r_pos+1] = False, True
            new_robot_pos.append(r_pos+1)
            is_robot[r_pos+1] = True
    robot_pos = new_robot_pos
    return

trial_num = 0
while True:
    trial_num += 1
    rotate()
    robot_moving()
    up_robot()
    if durability.count(0) >= K:
        break
print(trial_num)