"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # The pythonic way, which I know the interviewer will not like.
        # return copy.deepcopy(node)
        if not node:
            return None
        
        old_to_new = {}
        visited = set()
        #dfs function to recreate and map the old to the new.
        def dfs(node):
            if node in visited:
                return
            else:
                visited.add(node)
                old_to_new[node] = Node(node.val)
                for nei in node.neighbors:
                    dfs(nei)
        # Explore all the old nodes
        dfs(node)
        
        #Map the neighbours.
        for old, new in old_to_new.items():
            for nei in old.neighbors:
                # fetch the newly created node, by accessing the old node, that maps
                # to the new node.
                new_nei = old_to_new[nei]
                new.neighbors.append(new_nei)

        return old_to_new[node]


        
        