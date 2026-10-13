class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        def dfs(i, visited):
            visited.add(i)

            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei, visited)
        
        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                components += 1
        
        return components

