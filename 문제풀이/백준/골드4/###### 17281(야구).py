from itertools import permutations as pm
def game(order, last_player, inning_num):
    global score
    out = 0
    player = last_player
    loo = []
    while out < 3:
        now_player = order[player]
        now_score = innings[inning_num][now_player]
        if now_score == 0:
            out += 1
        else:
            for i in range(len(loo)):
                if loo[i] + now_score > 3:
                    score += 1
                    loo.pop(i)
            loo.append(now_score)
        player = (player + 1) % 9
    return player
N = int(input())
innings = [list(map(int,input().split())) for _ in range(N)]
def player_order():
    order_list = []
    for permu in pm(range(9),9):
        if permu[3] == 0:
            order_list.append(permu)
    # print(order_list)
    # print(len(order_list))
    return order_list
max_score = 0
order_list = player_order()
for order in order_list:
    last_player = 0
    score = 0
    for i in range(N):
        last_player = game(order, last_player, i)
    if score > max_score:
        max_score = score
print(max_score)