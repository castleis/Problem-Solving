# leetcode 543
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxx = 0
    result = 0
    def diameterOfBinaryTree(root):
        # 왼쪽 자식 : 2*n+1, 오른쪽 자식 : 2*(n+1)
        def findleef(node,d):
            if not node:
                return
            d += 1
            findleef(node.left,d)
            findleef(node.right,d)
            self.maxx = max(self.maxx, d)
            self.result += self.maxx
            self.maxx = 0
            return 

        findleef(root,0)
        return self.result

# Solution
class Solution:
    longest = 0
    def diameterOfBinaryTree1(root):
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left+right+2)
            return max(left,right)+1
        dfs(root)
        return self.longest
            