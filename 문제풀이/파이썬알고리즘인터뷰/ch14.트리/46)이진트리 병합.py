# leetcode 617
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(root1, root2):
        if not root1 and not root2:
            return
        if root1 and root2:
            root1.val += root2.val
        elif not root1:
            root1 = root2
        elif not root2:
            root2 = TreeNode()

        self.mergeTrees(root1.left, root2.left)
        self.mergeTrees(root1.right, root2.right)

        return root1

# 내 의도는!! root1를 뼈대로 root2를 추가하려고 했던 것이었는데 root1은 완전이진트리가 아니기 때문에... 딱 root1이 있는 구간만 병합하고 끝나버린다 ㅠㅠ
# 새로운 트리를 만들어야하는 것 같다
class Solution:
    def mergeTrees(root1, root2):
        node = TreeNode()
        # root1과 root2가 존재할때만 재귀를 진행해준다
        if root1 and root2:
            node.val = root1.val + root2.val
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        # 만약 root1이 null이라면 root2를 return하고
        elif not root1:
            return root2
        # root2가 null이라면 root1을 return
        elif not root2:
            return root1
