# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산
'''
입력 : [0,1,0,2,1,0,1,3,2,1,2,1]
출력 : 6
'''
height = list(map(int,input().split()))
# i가 현재 위치, j가 앞으로 이동하면서 계산
i,j = 0,0
rains = 0
while j < len(height):
    if height[i] == 0:
        i += 1
    else:
        h = height[i]
        j = i+1
        print(f'======위치 : {i}======')
        while j < len(height):
            if height[i] == max(height[i:]) and height[i] not in height[i+1:]:
                print(f'이후로 가장 큰 빌딩 : {i}')
                i += 1
                j += 1
                break
            if h > height[j]:
                rains += h-height[j]
                print(f' {j} : {rains}')
                j += 1
            elif h <= height[j]:
                i = j
                print(f'더 큰 빌딩을 만났다 : {i}')
                break
print(rains)

# Sol1. 투 포인터를 최대로 이동
