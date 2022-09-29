# leetcode 110
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
더이상 자식 노드가 없으면 0을 리턴, 
부모노드에서 left, right는 각각 왼쪽 자식의 깊이, 오른쪽 자식의 깊이 -> 둘 중 더 큰 값이 (현재 부모노드의 깊이 -1) 이므로
max(left,right) + 1을 리턴한다.
만약 left나 right가 -1이라면 이미 도 서브트리 간의 높이 차이가 존재하므로 더이상 회복되지 않음 -> 계속 -1을 리턴
'''
class Solution:
    def isBalanced(self, root):
        def check(root):
            # 값이 없다면 0을 return
            if not root:
                return 0
            # 왼쪽 자식 탐색
            left = check(root.left)
            # 오른쪽 자식 탐색
            right = check(root.right)

            # 두 레벨 차이가 1이 넘거나 각각이 -1이라면 바로 -1을 return
            if abs(left-right) > 1 or left == -1 or right == -1:
                return -1
            # 위의 조건문들에 해당이 안되면, 현재 노드의 높이를 계산하기 위해 left,right 중에서 큰 값 + 1을 return
            return max(left,right) + 1

        return check(root) != -1