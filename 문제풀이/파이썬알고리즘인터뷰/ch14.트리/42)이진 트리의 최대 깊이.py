# leetcode 104
from collections import deque
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution:
    def maxDepth(root):
        q = deque()
        depth = 0
        if root:
            q.append(root)
            while q:
                depth += 1
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
        return depth