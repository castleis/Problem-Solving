from collections import deque
from pprint import pprint

def making_group():
    visited = [[0]*grid_size for _ in range(grid_size)]
    group_num = 0
    for i in range(grid_size):
        for j in range(grid_size):
            if not visited[i][j]:
                same_group = [(i,j)]
                value = original_map[i][j]
                group_status_map[i][j] = group_num
                visited[i][j] = 1
                queue = deque([(i,j)])
                while queue:
                    x,y = queue.popleft()
                    for d in range(4):
                        nx, ny = x+dx[d], y+dy[d]
                        if 0 <= nx < grid_size and 0 <= ny < grid_size and not visited[nx][ny]:
                            if original_map[nx][ny] == value:
                                queue.append((nx,ny))
                                same_group.append((nx,ny))
                                group_status_map[nx][ny] = group_num
                                visited[nx][ny] = 1

                group_pos.append(same_group)
                group_value[group_num] = value
                group_num += 1
    print(group_num)
    return

def score_calculation():
    visited = [[[0]*4 for _ in range(grid_size)] for _ in range(grid_size)]
    score = 0
    for x in range(grid_size):
        for y in range(grid_size):
            cur_group_num = group_status_map[x][y]
            for d in range(4):
                nx,ny = x+dx[d], y+dy[d]
                if 0 <= nx < grid_size and 0 <= ny < grid_size:
                    next_group_num = group_status_map[nx][ny]
                    # print(f'cur_group_num : {cur_group_num}, next_group_num : {next_group_num} => {(len(group_pos[cur_group_num]) + len(group_pos[next_group_num])) * group_value[cur_group_num] * group_value[next_group_num]}')
                    if next_group_num != cur_group_num:
                        score += (len(group_pos[cur_group_num]) + len(group_pos[next_group_num])) * group_value[cur_group_num] * group_value[next_group_num]
                        # print(f'score up : {score}')
                    # visited[nx][ny][d] = 1
                    # visited[x][y][(d+2)%4] = 1
                    # print(f'===== {d}방향 : [{x},{y}], {visited[x][y]} -> [{nx},{ny}], {visited[nx][ny]} ======')
    # print('score : ',score)
    return score//2

def cross_counterclockwise_rotate():
    # original_map에서 진행
    half_grid_size = grid_size // 2
    for i in range(half_grid_size):
        temp = original_map[i][half_grid_size]
        original_map[i][half_grid_size] = original_map[half_grid_size][grid_size-1-i]
        original_map[half_grid_size][grid_size-1-i] = original_map[grid_size-1-i][half_grid_size]
        original_map[grid_size-1-i][half_grid_size] = original_map[half_grid_size][i]
        original_map[half_grid_size][i] = temp
    return

def clockwise_rotate():
    small_grid_size = grid_size//2
    for start_x,start_y in [(0,0),(0,small_grid_size+1),(small_grid_size+1,0),(small_grid_size+1,small_grid_size+1)]:
        half_grid_size = small_grid_size // 2
        # if half_grid_size % 2:
        #     column_size = half_grid_size+1
        # else:
        #     column_size = half_grid_size
        for col in range(half_grid_size if half_grid_size % 2 else half_grid_size+1):
            for row in range(half_grid_size):
                # print(f'========== {row},{col}')
                # print(f'[{start_x+row},{start_y+col}] -> [{start_x+(small_grid_size-1)-col}, {start_y+row}] -> [{start_x+(small_grid_size-1)-row}, {start_y+(small_grid_size-1)-col}] -> [{start_x+col},{start_y+(small_grid_size-1)-row}]')
                temp = original_map[start_x+row][start_y+col]
                original_map[start_x+row][start_y+col] = original_map[start_x+(small_grid_size-1)-col][start_y+row]
                original_map[start_x+(small_grid_size-1)-col][start_y+row] = original_map[start_x+(small_grid_size-1)-row][start_y+(small_grid_size-1)-col]
                original_map[start_x+(small_grid_size-1)-row][start_y+(small_grid_size-1)-col] = original_map[start_x+col][start_y+(small_grid_size-1)-row]
                original_map[start_x+col][start_y+(small_grid_size-1)-row] = temp
    return

grid_size = int(input())
original_map = [list(map(int,input().split())) for _ in range(grid_size)]
dx = [1,0,-1,0]  # [상,우,하,좌]
dy = [0,1,0,-1]
total_art_score = 0
for i in range(4):
    print(f'==================== {i}회차 ===========================')
    for k in range(grid_size):
        print(original_map[k])
    group_pos = []
    group_value = dict()
    group_status_map = [[0]*grid_size for _ in range(grid_size)]
    making_group()
    # print('그룹 갯수 : ', len(group_pos))
    # print(group_value)
    # print(group_pos)
    # print(group_status_map)
    total_art_score += score_calculation()
    cross_counterclockwise_rotate()
    clockwise_rotate()
    print()
    for k in range(grid_size):
        print(original_map[k])
# print()
print(total_art_score)
'''
7
1 2 3 4 5 6 7
8 9 10 11 12 13 14
15 16 17 18 19 20 21 
22 23 24 25 26 27 28 
29 30 31 32 33 34 35
36 37 38 39 40 41 42
43 44 45 46 47 48 49
'''
'''
15
1 2 3 4 5 6 7 0 1 2 3 4 5 6 7
8 9 10 11 12 13 14 0 8 9 10 11 12 13 14
15 16 17 18 19 20 21 0 15 16 17 18 19 20 21 
22 23 24 25 26 27 28 0 22 23 24 25 26 27 28 
29 30 31 32 33 34 35 0 29 30 31 32 33 34 35
36 37 38 39 40 41 42 0 36 37 38 39 40 41 42
43 44 45 46 47 48 49 0 43 44 45 46 47 48 49
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
1 2 3 4 5 6 7 0 1 2 3 4 5 6 7
8 9 10 11 12 13 14 0 8 9 10 11 12 13 14
15 16 17 18 19 20 21 0 15 16 17 18 19 20 21 
22 23 24 25 26 27 28 0 22 23 24 25 26 27 28 
29 30 31 32 33 34 35 0 29 30 31 32 33 34 35
36 37 38 39 40 41 42 0 36 37 38 39 40 41 42
43 44 45 46 47 48 49 0 43 44 45 46 47 48 49

'''

'''
29
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2 1 10 9 8 7 6 5 4 3 2
'''