import sys
sys.stdin = open('문제풀이/SWEA/4831.txt','r')

T = int(input())
for t in range(1,T+1):
    k,n,m = map(int, input().split())
    s = list(map(int, input().split()))
    # 연산을 편하게 하기 위해서 출발지와 도착지를 추가해줍니다.
    s.append(n)
    s.insert(0,0)

    # 배터리와 충전횟수
    battery= k
    cnt = 0

    for i in range(1,len(s)-1):
        # 버스가 이동한만큼 빼줍니다.
        battery -= (s[i]-s[i-1])
        print(f'정거장 : {s[i]}, 현재 배터리 : {battery}, 다음 정거장까지 거리 : {s[i+1]-s[i]}')
        # 현재 배터리가 다음 정거장까지의 거리보다 작다면
        if battery < s[i+1]-s[i]:
            # 그리고 배터리를 충전했을 때 다음 정거장까지 갈 수 있다면
            if k >= s[i+1]-s[i]:
                # 충전을 합니다.
                cnt += 1
                battery = k
                print(f'충전된 배터리 : {battery}, 충전 횟수 : {cnt}')
            # 충전을 해도 다음 정거장까지 갈 수 없다면
            else:
                # 충전 횟수를 0으로 바꾸고 종료합니다.
                cnt = 0
                break
    print(f'#{t} {cnt}')


# 다른 사람의 Solution. Bus를 한칸씩 이동시킨 코드
import sys

sys.stdin = open('문제풀이/SWEA/4831.txt')

T = int(input())

for t in range(1, T+1):
    '''
    K : 한 번 충전으로 최대 이동 횟수
    N : 종점
    M : 충전기 설치된 정류장 수
    '''
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    energy = K
    cnt = 0
    bus = 0

    while True:
        bus += 1
        energy -= 1

        if bus in station :
            if bus == station[0] :
                station.pop(0)
                # 다음 정류장이 없으면 종점 추가
                if not station :
                    station.append(N)

            # 다음 정류장과 최대 이동 횟수 비교해서 충전
            if energy < station[0]-bus :
                energy = K
                cnt += 1

        if bus == N : # 버스가 종점에 도착
            break
        elif not energy : # 도착하기 전에 이동 횟수 소진
            cnt = 0
            break

    print(f'#{t} {cnt}')

