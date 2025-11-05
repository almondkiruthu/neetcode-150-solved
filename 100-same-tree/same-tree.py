# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(node, frontier):
            if not node:
                frontier.append(None)
                # No node no need to process it further.
                return
            frontier.append(node.val)
            inorder(node.left, frontier)
            inorder(node.right, frontier)
        
        p_nodes = []
        inorder(p, p_nodes)
        q_nodes = []
        inorder(q, q_nodes)

        return p_nodes == q_nodes
        
       