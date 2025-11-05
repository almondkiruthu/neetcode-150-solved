# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def dfs(node):
            if not node:
                return 0
            else:
                depth_left = dfs(node.left)
                depth_right = dfs(node.right)
                diff = depth_left - depth_right
                if abs(diff) > 1:
                    self.isBalanced = False
                return max(depth_left, depth_right) + 1  
        
        dfs(root)
        return self.isBalanced == True

