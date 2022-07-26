T = int(input())
for t in range(1,T+1):
    N = list(map(int, input().split()))
    s = list(map(int, input().split()))
    k,n,m = N[0], N[1], N[2]
    s.append(n)


    battery= k
    cnt = 0
    i = 0  #버스의 위치
    while i < n:
        # 버스가 한칸씩 움직일 때마다(i += 1) battery 는 하나씩 빼주고
        battery -= 1
        i += 1
        print(f'정류장의 위치 : {i}, 도착했을 때 배터리 : {battery}')

        if battery < 0 :
            print(f'#{t} 0')
            break
        # 버스가 충전기가 있는 정류소에 도착했을 때
        if i in s:
            # 현재 배터리에서 다음 정류장까지의 소비량을 뺏을 때 0보다 작다면 배터리를 충전
            #(다음 정류장으로 가기 전에 battery가 0 이하가 되면)
            try:
                if battery - (s[s.index(i)+1]-i) < 0 :
                    print(f'다음 충전소까지 거리: {s[s.index(i)+1]-i}')
                    cnt += 1
                    print(f'{i}번째 정류장에서 총 충전횟수 : {cnt}')
                    battery += k
                    print(f'{i}번째 정류장을 출발할때 배터리 : {battery}')
            except:
                continue
    
    if battery < 0:
        continue
    else:
        print(f'#{t} {cnt}')

'''
다른 방법으로는 일단 종점까지 가야하는 배터리를 변수로 두고, 다음 정류장 갈 때마다 -1
충전소마다 +k 하고 그 때 배터리와 충전배터리를 비교해서 ... 
너무 복잡하게 생각하나?? 집에 갈 수 있는 간단한 조건을 생각해바받자ㅏ러니런ㅇ;맃;ㄹ
'''
