# 두번째 숫자 i에 따른 temp의 길이와 temp를 담아줄 딕셔너리
arr = {}
N = int(input())
i = 0

while i < N+1:
    temp = [N,i]
    while True:
        new = temp[-2] - temp[-1]
        # print(f'new : {new}')
        # new가 0보다 크거나 같다면 temp 리스트에 추가해줍니다.
        if new >= 0:
            temp.append(new)
            # print(f'{i} : {temp}')
        # new가 0보다 작다면 arr에 현재 temp의 길이, temp를 키 i의 value로 넣어줍니다.
        else:
            arr[i] = (len(temp), temp)
            break
    i += 1
# values에서 max값
ans = max(arr.values())
# max length 출력
print(ans[0]) 
for j in ans[1]:
    print(j, end=' ')