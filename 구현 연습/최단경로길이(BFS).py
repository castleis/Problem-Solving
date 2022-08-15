# (https://blog.hexabrain.net/269)
# 노션에 정리해두었다!
'''
6
1 1 1 1 1 1
0 0 1 0 0 1
1 1 1 0 1 1
1 0 0 0 1 0
1 1 1 0 1 0
0 0 1 1 1 1    # 최단 경로 길이: 13
'''
N = int(input())
mapp = []
x,y,l = [0]*100,[0]*100,[0]*100
# 큐에 좌표 정보와 길이를 삽입하는 함수
def enqueue(a,b,c):
    x[cnt] = a
    y[cnt] = b
    l[cnt] = c
    cnt += 1

def BFS(x,y):
    pos = 0
    cnt = 0 
    # 시작점의 좌표 정보를 큐에 삽입
    enqueue(x,y,1)

    # 더이상 방문할 지점이 없거나 도착지점에 도착하면 루프를 탈출
    while pos < cnt and (x[pos] != N-1 or y[pos] != N-1):
        # 두 번 방문하는것을 방지하기 위해 이미 지나갔다는 표시로 0으로 바꿔줌
        mapp[y[pos]][x[pos]] = 0

        # 위로 갈 수 있다면 위 지점의 좌표 정보와 길이를 큐에 삽입
        if y[pos] > 0 and mapp[y[pos]-1][x[pos]] == 1:
            enqueue(x[pos],y[pos]-1, l[pos]+1)
        # 아래로 갈 수 있다면 아래 지점의 좌표 정보와 길이를 큐에 삽입
        if y[pos] < N-1 and mapp[y[pos]+1][x[pos]] == 1:
            enqueue(x[pos],y[pos]+1, l[pos]+1)
        #왼쪽으로 갈 수 있다면 왼쪽의 좌표 정보와 길이를 큐에 삽입
        if x[pos] > 0 and mapp[y[pos]][x[pos]-1] == 1:
            enqueue(x[pos]-1,y[pos], l[pos]+1)
        if x[pos] < N-1 and mapp[y[pos]][x[pos]+1] == 1:
            enqueue(x[pos]+1,y[pos], l[pos]+1)

        # 큐의 다음 순서 지점을 방문
        pos += 1

    # cnt가 pos보다 크다면 도착 지점에 무사히 도착한 것.
    # 위의 반복문은 도착점에 도착하게 되면 루프를 바로 빠져나오기 때문에
    # 길이를 삽입하는 큐의 마지막 요소가 최단 경로의 길이라고 할 수 있다.
    if pos < cnt:
        print(f'최단 경로 길이 : {l[pos]}')

def main():
    for i in range(N):
        mapp.append(list(map(int,input().split())))
    BFS(0,0)
    return 0

print(main())