# leetcode 687
class Solution:
    longest = 0
    def longestUnivaluePath(root):
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else: left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else: right = 0
            
            self.longest = max(self.longest, left+right)
            return max(left,right)
        
        dfs(root)
        return self.longest