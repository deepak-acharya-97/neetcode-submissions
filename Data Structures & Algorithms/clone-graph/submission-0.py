"""
https://neetcode.io/problems/clone-graph
"""
from typing import Optional

"""
# Definition for a Node.

"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        old_to_new_map = {}
        def clone(node):
            if not node:
                return node
            if node in old_to_new_map:
                return old_to_new_map[node]
            cloned_node = Node(node.val)
            old_to_new_map[node] = cloned_node
            for n in node.neighbors:
                cloned_node.neighbors.append(clone(n))
            return cloned_node
        return clone(root)
