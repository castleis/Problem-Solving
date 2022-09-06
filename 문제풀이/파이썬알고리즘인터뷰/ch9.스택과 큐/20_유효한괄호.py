# 리트코드 20

def isValid(s):
        dict = {')':'(', ']':'[', '}':'{'}
        stack = []
        print(dict[']'])
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i in dict.keys():
                    if dict[i] == stack[-1]:
                        stack.pop()
                        continue
                stack.append(i)

        if not stack:
            return True
        else:
            return False

s = '([)]'
print(isValid(s))

# Sol 1 스택 일치 여부 판별
'''
(,[,{ 는 스택에 push 하고 ),],} 을 만났을 때 pop한 결과가 매핑 테이블 결과와 매칭되는지 확인
먼저 매핑 테이블을 만들어 놓고 테이블에 존재하지 않으면 무조건 push하고 pop햇을 때 결과가 일치하지 않으면 False를 리턴
파이썬 리스트의 push와 pop은 O(1)에 동작
'''
def isValid1(s):
    stack = []
    table = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
    }
    for char in s:
        if char not in table:
            stack.append(char)
        # table에 존재하지 않는데 스택이 비어있다면 무조건!!! 평생!!! 짝이 없는 것이므로 return False
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack)==0