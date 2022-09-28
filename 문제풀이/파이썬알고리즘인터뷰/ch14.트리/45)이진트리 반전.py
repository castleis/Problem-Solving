# leetcode 226

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(root):
        def dfs(node):
            if not node:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)

            helper = TreeNode()
            helper = node.left
            node.left = node.right
            node.right = helper
            return node

        dfs(root)
        return root