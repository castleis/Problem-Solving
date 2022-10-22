# leetcode 148
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 병합 정렬 풀이
# 320 ms
class Solution:
    def mergesort(self,l1,l2):
            if l1 and l2:
                if l1.val > l2.val:
                    l1,l2 = l2,l1
                # l1의 포인터를 이동하면서 정렬해 리턴
                l1.next = self.mergesort(self,l1.next,l2)
            # 둘 중 하나가 없으면 있는 값을 리턴
            return l1 or l2

    def sortList(self, head):

        front, mid, end = head, None, head
        # runner 기법 : front는 한칸씩, end는 두칸씩
        while end and end.next:
            mid, front, end = front, front.next, end.next.next
        mid.next = None            # mid를 기준으로 연결리스트 끊기

        l1 = self.sortList(head)
        l2 = self.sortList(mid)

        return self.mergesort(l1,l2)

# 내장함수를 이용하는 실용적인 방법
# 85ms
class Solution1:
    def sortList(self, head):
        # 먼저 연결 리스트를 파이썬 리스트로 변환
        # p : 포인터, 연결리스트를 순회하며 값을 채워넣는 역할
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next
        
        # 정렬
        lst.sort()

        # 파이썬 리스트를 연결리스트로 변환 
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head