# leetcode 706
'''
put(key, value) : 키, 값을 해시맵에 삽입. 만약 이미 존재하는 키라면 업데이트!
get(key) : 키에 해당하는 값 조회. 만약 키가 존재하지 않는다면 -1 리턴
remove(key) : 키에 해당하는 키, 값을 해시맵에서 삭제
'''
# 개별 체이닝 방식을 이용한 해시 테이블 구현
'''
편의상 키와 값은 모두 int
키, 값을 보관하고 연결 리스트로 처리할 별도의 객체 구현 -> ListNode라는 이름의 클래스 정의
'''
import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    # 초기화 구현
    def __init__(self):
        self.size = 1000
        # 존재하지 않는 키를 조회할 경우 자동으로 디폴트를 생성하도록 collections.defaultdict 사용
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 해당 인덱스에 값에 아무것도 없다면 삽입하고 리턴
        if self.table[index].value == None:
            self.table[index] = ListNode(key,value)
            return
        
        # 해당 인덱스에 이미 있다면! p는 이미 존재하고 있는 값
        p = self.table[index]
        # p에 연결되어 있는 값들을 while문을 따라 조회
        while p:
            # 1. key 값이 같다면 value를 업데이트하고 리턴
            if p.key == key:
                p.value = value
                return
            # 2. next에 아무것도 없다면 종료
            if p.next == None:
                break
            # 다음 연결리스트로 넘어감
            p = p.next
        # key값이 같은 것도 없고 + 연결리스트의 끝이므로 삽입 해준다
        p.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = key % self.size
        # 해당 index에 value가 없다면 -1 리턴
        if self.table[index].value == None:
            return -1
        p = self.table[index]
        # while문을 따라 연결리스트를 순회하면서 키값이 같으면 value 리턴
        while p:
            if p.key == key:
                return p.value
            p = p.next
        # 끝까지 순회했음에도 타겟을 찾지 못했으면 -1 리턴
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
    
        if self.table[index].value == None:
            return
        
        p = self.table[index]
        if p.key == key:
            # 인덱스의 첫번째 노드에 삭제하고자 하는 값이 있을 때 
            if p.next == None:
                self.table[index] = ListNode()
            else:
                p = p.next
            return
        prev = p
        while p:
            if p.key == key:
                # 이전 노드의 next에 p의 next를 연결 -> 현재 노드 삭제
                prev.next = p.next
                return
            prev,p = p, p.next