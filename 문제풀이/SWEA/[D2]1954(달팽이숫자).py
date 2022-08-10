# import sys
# sys.stdin = open('')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr1 = [N]
    for i in range(1,N):
        arr1.extend([N-i, N-i])
    # print(arr1)
    d = [1,1,-1,-1]
    x,y = 0,-1
    location = 0
    num = 0
    stopp = False
    for j in range(len(arr1)):
        if stopp == True:
            break
        for i in range(arr1[j]):
            num += 1
            if j % 2 == 0 :
                y += d[location]
                arr[x][y] = num
            else :
                x += d[location]
                arr[x][y] = num
            if num == N*N:
                stopp = True
                break
            # print(f'{j},{location}   {x},{y} : {arr}')
        location = (location + 1) % 4
    print(f'#{t}')
    for c in range(N):
        print(*arr[c])

# SWEA에서 볼만한 풀이 : 메모리 사용량, 소요 시간 모두 적은 편이었다.
# d를 만들지 않고, 상황에 따라 s값을 바꿔서 s값에 따라 움직이도록 만들었다.
# s의 움직임 방향 : 오른쪽(0)->아래(1)->왼쪽(2)->위(3)->오른쪽(0)-> ...
for a in range(int(input())):
    n=int(input())
    m=[]
    for i in range(n):
        m.append([0 for i in range(n)])
    x=y=s=0
    for j in range(n*n):
        m[x][y]=j+1
        # s가 0일 때는 오른쪽으로 감
        if s==0:
            # y가 범위 밖으로 나가거나 해당 위치에 이미 값이 있을 때는 s를 1로 바꿔주고 x +1
            if y+1>=n or m[x][y+1]>0:
                s=1
                x+=1
            else:
                y+=1
        # s가 1일 때는 아래로 감
        elif s==1:
            if x+1>=n or m[x+1][y]>0:
                s=2
                y-=1
            else:
                x+=1
        # s가 2일 때는 왼쪽으로 감
        elif s==2:
            if y-1<0 or m[x][y-1]>0:
                s=3
                x-=1
            else:
                y-=1
        #s가 3일 때는 위로 감
        elif s==3:
            if x-1<0 or m[x-1][y]>0:
                s=0
                y+=1
            else:
                x-=1
    print(f'#{a+1}')
    for j in m:
        print(' '.join(map(str,j)))