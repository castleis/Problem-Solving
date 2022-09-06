# leetcode 225
'''
큐를 이용해 다음 연산을 지원하는 스택 구현
push(x)
pop()
top()
empty()
'''
class MyStack:

    def __init__(self):
        self.stack = []
        pass

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
      

    def empty(self) -> bool:
        return not self.stack

# Sol1 : push(x)할 때 큐를 이용해 재정렬
import collections
class MyStack1:
    def __init__(self):
        self.q = collections.deque()
    
    def push(self,x):
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0