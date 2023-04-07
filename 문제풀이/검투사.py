def find_gun(x,y,i):
    global gun_map
    if len(gun_map[x][y]) > 0:
        gun_list = gun_map[x][y] + [player_gun[i]]
        max_power_gun = max(gun_list)
        if player_gun[i] > 0:
            gun_map[x][y].append(player_gun[i])
        player_gun[i] = max_power_gun
        gun_map[x][y].remove(max_power_gun)
    return

def main_action(player):
    # 이동 방향으로 한 칸 이동
    x,y = player_pos[player]
    d = player_dir[player]
    dx,dy = directions[d]
    nx,ny = x+dx, y+dy
    if nx < 0 or nx >= grid_size or ny < 0 or ny >= grid_size:
        d = (d + 2) % 4  # 벽에 막히면 반대방향으로 되돌아가기
        player_dir[player] = d
        dx, dy = directions[d]
        nx, ny = x+dx, y+dy
    # print(f'출발 위치 : [{x},{y}] -> 다음 위치 : [{nx},{ny}]')
    # 이동한 위치 (nx, ny)에서 다른 플레이어가 있는지
    if not player_map[nx][ny]:
        find_gun(nx,ny,player)
        player_map[x][y], player_map[nx][ny] = 0, player
        player_pos[player] = (nx,ny)
    
    else:
        fighter = player_map[nx][ny]
        # print(f'{player} : [{player_power[player]} + {player_gun[player]}],,,,,, {fighter} : [{player_power[fighter]} + {player_gun[fighter]}]')
        powers = [player_power[player]+player_gun[player], player_power[fighter]+player_gun[fighter]]
        if powers[0] > powers[1]:
            winner, looser = player, fighter
        elif powers[0] < powers[1]:
            winner, looser = fighter, player
        else:
            if player_power[player] > player_power[fighter]:
                winner, looser = player, fighter
            else:
                winner, looser = fighter, player
        # print('winner : ', winner, 'looser : ', looser)
        # print(f"{player}'s power : ",powers[0], f"{fighter}'s power : ", powers[1])
        scores[winner] += abs(powers[0]-powers[1])

        # 현재 플레이어가 winner라면 현재 위치 (nx, ny)로 옮겨줌
        # if winner == player:
        player_map[x][y], player_map[nx][ny] = 0, winner
        player_pos[winner] = (nx,ny)
        looser_action(nx,ny,looser)
        find_gun(nx,ny,winner)
    return

def looser_action(x,y,player):
    gun_map[x][y].append(player_gun[player])  # 들고 있던 총 내려놓고
    player_gun[player] = 0
    # 한 칸 이동
    dx,dy = directions[player_dir[player]]
    nx,ny = x+dx, y+dy
    while nx < 0 or nx >= grid_size or ny < 0 or ny >= grid_size or player_map[nx][ny] > 0:
        player_dir[player] = (player_dir[player] + 1) % 4
        dx, dy = directions[player_dir[player]]
        nx, ny = x+dx, y+dy
    
    player_map[nx][ny] = player
    player_pos[player] = (nx,ny)
    find_gun(nx,ny,player)
    return

# def winner_action(x,y,nx,ny,player):
#     find_gun(nx,ny,player)
#     player_map[x][y], player_map[nx][ny] = 0, player
#     player_pos[player] = (nx,ny)
#     return

grid_size, player_num, round_num = map(int,input().split())
gun_map = [[[int(n)] if int(n) > 0 else [] for n in input().split()] for _ in range(grid_size)]
# print('gun_map : ', gun_map)
player_power = [0]*(player_num+1)
player_gun = [0]*(player_num+1)
player_dir = [0]*(player_num+1)
player_pos = [(False,False)]
player_map = [[0]*grid_size for _ in range(grid_size)]
scores = [0]*(player_num+1)
directions = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}

for i in range(1,player_num+1):
    x,y,d,s = map(int,input().split())
    player_pos.append((x-1, y-1))
    player_map[x-1][y-1] = i
    player_dir[i] = d
    player_power[i] = s
trial = 0
while trial < round_num:
    # print(f'************************************************** {trial} *********************************************************')
    for i in range(1,player_num+1):
        # print(f'============================== {i}번 플레이어 =============================')
        main_action(i)
        # print("player_pos : ", player_pos)
        # print("player_gun : ", player_gun)
        # print("player_map : ", player_map)
        # print("gun_map : ", gun_map)
        # print("scores : ", scores)
        # print()
    trial += 1
print(*scores[1:])
'''
5 4 1
1 2 0 1 2
1 0 3 3 1
1 3 0 2 3
2 1 2 4 5
0 1 3 2 0
1 3 2 3
2 2 1 5
3 3 2 2
5 1 3 4

'''