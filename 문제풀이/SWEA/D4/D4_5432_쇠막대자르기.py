import sys
sys.stdin = open('0812\\5432.txt')

''' 제한시간 초과ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ'''
'''
T = int(input())
for t in range(1,T+1):
    strr = input()
    i,j = 0,1 # i는 현재 인덱스 / j는 앞으로 가면서 비교할 애들 인덱스?
    blocks = []
    while i < len(strr):
        if strr[i] == '(':
            # print(f'탐색시작 {i}')
            laser = 0
            a,b = 1,0    # a: '(' 개수, b: ')' 개수
            for j in range(i+1,len(strr)):
                if strr[j] == '(':
                    a += 1
                    if strr[j+1] == ')':
                        laser += 1
                elif strr[j] == ')':
                    b += 1

                if a == b :
                    # print(a,b)
                    # print(f'막대 [{i},{j}], laser : {laser}')
                    if laser:
                        blocks.append(laser+1)
                    break
        i += 1
    print(f'#{t} {sum(blocks)}')
'''

# =======================================================================
def blocks(arr):
    unclosed = []
    block = 0
    i = 0
    while i < (len(arr)):
        # print(f'현재 탐색 위치는 {i}')
        if arr[i] == '(':
            # 레이저일 때
            if arr[i+1] == ')':
                block += len(unclosed)
                # print(i, block)
                i += 1
            # 레이저가 아니라면 아직 닫히지 않았기 때문에 unclosed에 추가
            else:
                unclosed.append(arr[i])
                # print(f'열림! {unclosed}')

        elif arr[i] == ')':
            if unclosed:
                unclosed.pop()
                # print(f'닫힘! {unclosed}')
                block += 1
                # print(i, block)
            else : 
                # print('해당사항 없다!!')
                continue
        i += 1
    return block

T = int(input())
for t in range(1,T+1):
    strr = input()
    ans = blocks(strr)
    print(f'#{t} {ans}')