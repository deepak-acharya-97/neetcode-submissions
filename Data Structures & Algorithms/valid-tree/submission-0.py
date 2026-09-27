"""
https://neetcode.io/problems/valid-tree
"""
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def approach_1():
            if len(edges) > n - 1:
                return False

            adj = [[] for _ in range(n)]
            for src, dest in edges:
                adj[src].append(dest)
                adj[dest].append(src)

            visited = set()

            def dfs(node, parent):
                if node in visited:
                    return False
                visited.add(node)
                for n in adj[node]:
                    if n == parent:
                        continue
                    if not dfs(n, node):
                        return False
                return True
            
            return dfs(0, -1) and len(visited) == n
        
        return approach_1()
