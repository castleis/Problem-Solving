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


strr = input()
print(blocks(strr))