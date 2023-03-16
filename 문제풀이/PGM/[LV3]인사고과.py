def solution(scores):
    wanho = scores[0]
    scores.sort(key = lambda x:x[0]+x[1], reverse=True)
    print(scores)
    max_x = max(x for x,y in scores)
    max_y = max(y for x,y in scores)
    if wanho[0] < max_x and wanho[1] < max_y:
        return -1
    print(max_x, max_y)
    pos = scores.index(wanho)
    print(pos)
    summation = [x+y for x,y in scores]
    print(summation)
    rank = 1
    for i in range(pos+1):
        X,Y = scores[i]
        if X < max_x and Y < max_y:
            print(f'{i} 돌아간다')
            continue
        print(f'======= {i} ========')
        if wanho[0] < X and wanho[1] < Y:
            return -1
        if summation[i] == summation[pos]:
            break
        rank += 1
        print(rank)
    # # answer = 0
    return rank

# scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]
# scores = [[1, 4], [4, 4], [3, 3], [5, 3], [1, 3]]
scores = [[3, 2], [2, 5], [5, 2], [4, 3]]
print(solution(scores))