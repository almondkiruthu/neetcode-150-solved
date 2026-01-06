# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]

        def search(root):
            if not root:
                return
            # set the current node to be our current LCA
            lca[0] = root
            if root is p or root is q:
                return
            # current node values are too small, therefore we set the lca to the right
            # and keep moving and vice versa on the left traversal
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            else:
                # we found the split point no need to dive in deeper in
                # the recursion
                return
        
        search(root)
        return lca[0]