# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # implement bfs.
        q = deque()
        q.append(root)
        res = []
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                curr_node = q.popleft()
                level.append(curr_node.val)
                if (curr_node.left):
                    q.append(curr_node.left)
                if (curr_node.right):
                    q.append(curr_node.right)
            
            res.append(level)

        return res
