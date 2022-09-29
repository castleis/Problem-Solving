# leetcode 297
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = ['#']
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            # node값이 있다면 left부터 q에 넣고, node.val을 출력 리스트에 추가해준다.
            if node:
                q.append(node.left)
                q.append(node.right)
                data.append(str(node.val))
            else:
                data.append('#')
        return ' '.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # data가 연속해서 #가 나온다면 자식 노드가 없다는 뜻이므로 return None
        if data == '# #':
            return None

        nodes = data.split()

        q = collections.deque()
        root = TreeNode(int(nodes[1]))
        q.append(root)
        # root의 왼쪽 자식부터 시작하기 위해 idx를 2로 설정
        idx = 2

        while q:
            node = q.popleft()
            # 왼쪽 자식 확인. #이 아니라면 node.left에 연결해주고 q에 추가. 
            # 후에는 오른쪽 자식을 확인해주기 위해 idx += 1
            if nodes[idx] != '#':
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx += 1
            # 오른쪽 자식 확인. #이 아니라면 node.right에 연결해주고 q에 추가
            # 후에는 왼쪽 자식을 확인해주기 위해 idx += 1
            if nodes[idx] != '#':
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx += 1
        return root