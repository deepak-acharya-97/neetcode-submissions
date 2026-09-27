"""
https://neetcode.io/problems/count-connected-components
"""
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = [[] for _ in range(n)]
        def dfs(node):
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)

        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
                
        return components

