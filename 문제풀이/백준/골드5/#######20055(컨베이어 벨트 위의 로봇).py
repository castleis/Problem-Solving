N,K = map(int,input().split())
durability = list(map(int,input().split()))
robot_pos = []             # 현재 로봇이 위치해있는 컨베이어 벨트의 인덱스들을 담아둘 리스트
up_pos, down_pos = 0, N-1  # 올리는 위치, 내리는 위치. 벨트가 회전할 때마다 *_pos - 1

def robot_moving():
    global robot_pos
    new_robot_pos = []
    while robot_pos:
        r_pos = robot_pos.pop(0)
        n_pos = r_pos + 1
        if n_pos == down_pos:       # 다음 위치가 내리는 위치라면 바로 삭제
                continue
        if n_pos not in robot_pos and durability[n_pos] > 0:   # 다음 위치에 로봇이 없고 내구도가 남아 있을 때만 이동
            durability[n_pos] -= 1              # 다음 위치의 내구도 -1
            # if durability[n_pos] == 0:              # 내구도가 깎인 다음 위치의 내구도가 0이라면 k_cnt + 1
            #     k_cnt += 1
            new_robot_pos.append(n_pos)     # new_robot_pos에 다음 위치 추가
        elif n_pos in robot_pos or durability[n_pos] == 0:
            new_robot_pos.append(r_pos)
    robot_pos = new_robot_pos
    return

def up_robot():
    if durability[up_pos] > 0:                  # 올리는 위치의 내구도가 0이 아닐 때
        robot_pos.append(up_pos)                    # robot_pos에 로봇 올리기
        durability[up_pos] -= 1
        # if durability[up_pos] == 0:              # 내구도가 깎인 다음 위치의 내구도가 0이라면 k_cnt + 1
        #     k_cnt += 1
    return

def rotate():
    global robot_pos
    robot_pos = [x+1 for x in robot_pos]
    try:
        robot_pos.remove(down_pos)
    except:
        pass
    last_du = durability.pop()
    durability.insert(0,last_du)
    return

trial_num = 0
while True:
    trial_num += 1
    print(f'======== {trial_num} =========')
    rotate()
    # print('after rotate       :', durability, robot_pos)
    robot_moving()
    # print('after robot_moving :', durability, robot_pos)
    up_robot()
    # print('after up_robot     :', durability, robot_pos)
    print()
    if durability.count(0) >= K:
        break
print(trial_num)