# leetcode 622
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.k = k
        self.front = 0
        self.rear = 0
        print(self.q)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            print(value, 'why?', self.front, self.rear)
            return False
        self.q[self.rear] = value
        print(f'rear : {self.rear}, value : {value}, {self.q}')
        self.rear = (self.rear + 1) % self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        print(f'front : {self.front}, {self.q}')
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]
        

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        # rear가 가리키는 인덱스의 다음 인덱스를 front가 가리키고 있다면 FUll
        return self.front == (self.rear + 1) % self.k