# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            # if current node value is greater than the maxValue we have seen so far
            # the it's a good_node.

            # Starting of from the root using preorder, at first it's 
            # good_node_count == 0
            good_node_count = 0
            if node.val >= max_val:
                good_node_count = 1
            
            max_val = max(max_val, node.val)
            good_node_count += dfs(node.left, max_val)
            good_node_count += dfs(node.right, max_val)
            
            return good_node_count

        return dfs(root, float("-inf"))
        