'''
맨 아래 행의 2를 찾아서 위로 올라가면서 탐색하면 어떨까유?
#1 67   o
#2 45   o
#3 39   o
#4 24   o
#5 91   o
#6 93   o
#7 90   o
#8 4    o
#9 99   o
#10 35  o

'''
import sys
sys.stdin = open('0811/1210.txt')
for _ in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start_point = []

    for i in range(100):
        if ladder[0][i] == 1:
            start_point.append(i)

    stopp = False
    for j in start_point:
        if stopp == True:
            break
        xidx = j
        yidx = 0

        while yidx < 99 :
            # print(f'{yidx},{xidx} : {ladder[yidx][xidx]}')
            yidx += 1
            if yidx == 99:
                # print(f'{j} 도착!!!!!!! 현재 높이, 위치 : {yidx}, {xidx}, {ladder[yidx][xidx]}')
                if ladder[yidx][xidx] == 2:
                    print(f'#{t} {j}')
                    stopp = True
                    break

            else:
                if 0 < xidx < 98:
                    # 오른쪽이 1이라면
                    if ladder[yidx][xidx+1] == 1:
                        # 그 다음 0이 나올 때까지 이동
                        # 병진님 풀이 : 그 다음 0이 나오는 구간은, 지금 있는 기둥의 옆 기둥까지 가면 되는건데
                        # 그 옆 기둥은, start_point의 인덱스끼리의 사이의 거리;;; ㅠ퓨ㅠㅠㅠㅠ 개쩐당
                        for c in range(xidx + 1 ,100):
                            if ladder[yidx][c] == 0:
                                xidx = c-1
                                break
                            if c == 99:
                                xidx = 99
                    
                    # 왼쪽이 1이라면
                    elif ladder[yidx][xidx-1] == 1:
                        for c in range(xidx-1 ,-1,-1):
                            if ladder[yidx][c] == 0:
                                xidx = c+1     
                                break
                            if c == 0:
                                xidx = 0

                elif xidx == 0:
                    if ladder[yidx][xidx+1] == 1:
                        for c in range(xidx + 1 ,100):
                            if ladder[yidx][c] == 0:
                                xidx = c-1
                                break
                    else:
                        continue

                elif xidx == 99:
                    if ladder[yidx][xidx-1] == 1:
                        for c in range(xidx-1 ,-1,-1):
                            if ladder[yidx][c] == 0:
                                xidx = c+1  
                                break 
                    else:
                        continue


#
for _ in range(10):
    t = int(input())

    ladder = [list(map(int, input().split())) for i in range(100)] # 사다리 그리기

    st = [] # 출발 지점 표시하기
    for i in range(100):
        if ladder[0][i] == 1:
            st.append(i)

    for i, p in enumerate(st): # 출발 지점에서 출발하기
        ans = p
        n = [0, p]
        while n[0] != 100:
            if (p != 0) and ladder[n[0]][p-1] == 1 : # 왼쪽길이 뚫린경우
                i -= 1
                p = st[i] # 출발점 인덱스 한 칸 왼쪽 위치로 이동
            elif (p != 99) and ladder[n[0]][p+1] == 1 : # 오른쪽 길이 뚫린경우
                i += 1
                p = st[i] # 출발점 인덱스의 한 칸 오른쪽 위치로 이동
            
            if ladder[n[0]][p] == 2:
                print(f"#{t} {ans}")
                break
            
            n[0] += 1 # 뚫린길이 없다면 아래로 이동
