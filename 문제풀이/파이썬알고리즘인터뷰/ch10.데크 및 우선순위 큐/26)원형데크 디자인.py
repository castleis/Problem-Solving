# leetcode 641
class ListNode:
    def __init__(self, n):
        self.value = n
        self.left = None
        self.right = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.k = k
        self.len = 0
        self.head.right, self.tail.left = self.tail, self.head
    
    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node:ListNode, new:ListNode):
        n = node.right
        # 현재 노드의 right = new
        node.right = new
        # new의 left는 현재 노드, right는 현재노드의 이전 right (n)
        new.left, new.right = node,n
        # n의 left를 new로 : node -> new -> n 연결
        n.left = new
    
    ## 질문질문
    def _del(self, node:ListNode):
        # node를 삭제하는건데 ...
        # node.right을 삭제한거 아님여???? @.@????
        prev = node.left
        next = node.right
        prev.right = next
        next.left = prev


    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        # n = self.tail.right이고, n.right가 없으니까... self.tail.left 넣는듯
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True        

    def getFront(self) -> int:
        if self.len > 0 :
            return self.head.right.value
        else:
            return -1

    def getRear(self) -> int:
        if self.len > 0:
            return self.tail.left.value
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k