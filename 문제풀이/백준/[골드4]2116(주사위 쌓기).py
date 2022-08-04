"""
인덱스 0-5 / 1-4 / 2-3 이 서로 마주봄
마주보는 숫자들은 최대한 작은 것을 고를 수 있도록 하자
(for문 1)맨 처음 주사위의 0번째 인덱스부터 밑바닥 시작 ~ 5번째 인덱스까지
(for문 2)그 다음 주사위의 밑바닥은 그 아래 주사위의 윗바닥의 값과 같은 것을 다음 주사위 리스트에서 찾기
        각 주사위마다 밑,윗바닥을 제외한 면들에서 가장 큰 값을 더해나감
각 시작점마다의 더한 값들 중 최댓값을 출력

마주보는 것 이외의 숫자 중 제일 큰 숫자를 더한 값을 인덱스에 넣어서 max 값을 찾는 것은 어떨까?
"""
import sys

N = int(sys.stdin.readline())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(info)

pair = {0 : [0,5], 1 : [1,3], 2 : [2,4] , 3 : [3,1], 4 : [4,2], 5 : [5,0]}
result = []

# print(info[pair[2][1]])   
for i in range(6):
    bottoms = []
    tops = []
    bottoms.append(info[0][i])
    tops.append(info[0][pair[i][1]])
    max_0lst = [1,2,3,4,5,6]
    max_0lst.remove(bottoms[0])
    max_0lst.remove(tops[0])
    max_0 = max(max_0lst)
    print(f'첫번째 주사위 밑,위 바닥 : {bottoms[0]} {tops[0]}, {max_0}')
    sums = 0
    for j in range(1,len(info)):
        num = [1,2,3,4,5,6]
        # line = info[j]
        # idx_b 는 밑바닥의 인덱스
        idx_b = info[j].index(tops[j-1])
        bottoms.append(info[j][idx_b])
        print(f'{j+1}번째 주사위의 밑바닥은 {bottoms[j]}')
        tops.append(info[j][pair[idx_b][1]])
        print(f'{j+1}번째 주사위의 위바닥은 {tops[j]}')
        num.remove(bottoms[j])
        num.remove(tops[j])
        sums += max(num)
        print(f'{j+1}번째 주사위의 최대 숫자는 {max(num)}, sums : {sums}')
    result.append(sums+max_0)
print(max(result))
