# 리트코드 739
def dailyTemperatures(temperatures) :
    stack = []
    result = [0]*len(temperatures)
    for i in range(len(temperatures)):
        # print(f'=========================')
        # print(f'현재는 : {i, temperatures[i]}')
        # print(f'stack : {stack}')
        if not stack:
            stack.append((i,temperatures[i]))
            continue
        for _ in range(len(stack)-1,-1,-1):
            idx,temp = stack[-1]
            # print(f' 비교대상 : {idx,temp}')
            if temperatures[i] > temp:
                # print('더 따뜻')
                stack.pop()
                result[idx] = i - idx
            # 어차피 stack[-1]이 현재 온도보다 크면 나머지도 다 크므로 더이상 진행하지 않고 종료
            else:
                break
        stack.append((i,temperatures[i]))
        # print(result)
    return result

T = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(T))

# Sol : 스택 값 비교
'''
현재의 인덱스를 계속 스택에 쌓아두다가, 
이전보다 상승하는 지점에서 현재 온도와 스택에 쌓아둔 인덱스 지점의 온도 차이를 비교해서 
더 높다면 스택 값을 pop으로 꺼내고 현재 인덱스와 스택에 쌓아둔 인덱스의 차이를 정답으로 처리
'''
def dailyTemperatures1(T):
    answer = [0]*len(T)
    stack = []
    # tbqkf!!! enumerate라는 좋은 함수가 있음을 잊지 말아주자... :(
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer