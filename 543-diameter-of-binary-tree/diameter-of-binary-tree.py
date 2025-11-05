# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0
            else:
                left_diameter = dfs(node.left)
                right_diameter = dfs(node.right)
                curr_diameter = left_diameter + right_diameter
                self.diameter = max(self.diameter, curr_diameter)
            # print("Value to be returned is", max(left_diameter, right_diameter) + 1, "at node", node.val)
            return max(left_diameter, right_diameter) + 1
        if not root:
            return 0
        else:
            dfs(root)
            return self.diameter
