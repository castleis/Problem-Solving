def tree_grow():
    for i in range(n):
        for j in range(n):
            if tree_map[i][j] > 0:
                growth_cnt = 0
                for di, dj in D_dir:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < n and 0 <= nj < n and tree_map[ni][nj] > 0:
                        growth_cnt += 1
                tree_map[i][j] += growth_cnt
    return

def tree_move():
    move_dict = dict()
    for i in range(n):
        for j in range(n):
            if tree_map[i][j] > 0:
                # print(f'======= [{i},{j}] =======')
                can_move_cnt = 0
                can_move_pos = []
                for di, dj in D_dir:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < n and 0 <= nj < n and tree_map[ni][nj] == 0:
                        can_move_cnt += 1
                        can_move_pos.append((ni,nj))
                # print('번식할 수 있는 칸들 : ', can_move_pos, '번식 숫자 : ', can_move_cnt)
                if can_move_cnt == 0:
                    continue
                move_num = tree_map[i][j] // can_move_cnt
                for ni,nj in can_move_pos:
                    if (ni,nj) in move_dict.keys():
                        move_dict[(ni,nj)] += move_num
                    else:
                        move_dict[(ni,nj)] = move_num
    # print('move_dict : ', move_dict)
    for move_pos, move_num in move_dict.items():
        i,j = move_pos
        tree_map[i][j] += move_num
    return

def tree_kill(diffuse_distance, consistence_year):
    max_tree_cnt = 0
    max_tree_pos = []
    for i in range(n):
        for j in range(n):
            if tree_map[i][j] > 0:
                # print(f'============= [{i},{j}] ===============')
                tree_cnt = tree_map[i][j]
                tree_pos = [(i,j)]
                for di, dj in D_dig:
                    ni, nj = i, j
                    for dis in range(diffuse_distance):
                        ni, nj = ni+di, nj+dj
                        if ni < 0 or ni >= n or nj < 0 or nj >= n:
                            break
                        elif -consistence_year <= tree_map[ni][nj] <= 0:
                            tree_pos.append((ni,nj))
                            break
                        elif tree_map[ni][nj] == -77:
                            break
                        elif tree_map[ni][nj] > 0:
                            tree_cnt += tree_map[ni][nj]
                            tree_pos.append((ni,nj))
                # print('박멸할 나무 개수 : ', tree_cnt, '박멸 나무 리스트 : ',tree_pos)
                if max_tree_cnt < tree_cnt:
                    max_tree_cnt = tree_cnt
                    max_tree_pos = tree_pos[:]
            # elif -consistence_year <= tree_map[i][j] < 0:
            #     tree_map[i][j] += 1
    # print('max_tree_pos : ', max_tree_pos)
    # print('max_tree_cnt : ', max_tree_cnt)
    for i in range(n):
        for j in range(n):
            if -consistence_year <= tree_map[i][j] < 0:
                tree_map[i][j] += 1
    for i,j in max_tree_pos:
        tree_map[i][j] = -consistence_year
    return max_tree_cnt

n,m,k,c = map(int,input().split())
tree_map = [list(map(int,input().split())) for eunseong in range(n)]
D_dir = [(1,0),(0,1),(-1,0),(0,-1)]
D_dig = [(1,1),(-1,1),(1,-1),(-1,-1)]
for i in range(n):
    for j in range(n):
        if tree_map[i][j] == -1:
            tree_map[i][j] = -77

year = 0
killed_trees_cnt = 0
while year < m:
    # print(f'===================== {year} =======================')
    tree_grow()
    # print('after grow - ', tree_map)
    tree_move()
    # print('after move - ', tree_map)
    killed_trees_cnt += tree_kill(k,c)
    # print('after kill - ', tree_map)
    # print()
    year += 1
print(killed_trees_cnt)

'''
11 446 20 3
0 0 0 -1 57 0 -1 0 0 0 0 
0 18 0 -1 -1 0 0 0 0 0 45 
64 0 10 0 0 -1 74 0 0 33 0 
0 61 0 0 -1 0 0 0 0 0 -1 
0 66 0 0 0 0 0 0 16 0 0 
7 0 0 0 6 0 0 -1 27 72 0 
0 0 0 0 0 54 0 42 -1 -1 0 
0 0 -1 0 0 0 0 1 0 0 98 
-1 98 68 0 0 75 1 93 0 0 0 
0 0 0 0 77 0 0 -1 0 0 0 
0 -1 0 -1 0 0 0 0 45 0 0 

'''