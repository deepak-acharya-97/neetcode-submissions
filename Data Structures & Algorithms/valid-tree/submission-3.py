class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjacency_list = [[] for i in range(n)]

        if len(edges) > n-1:
            return False

        for src, dest in edges:
            adjacency_list[src].append(dest)
            adjacency_list[dest].append(src)
        
        def dfs(i, parent, visited, callstack):
            if i not in visited:
                visited.add(i)
                result = True
                for nei in adjacency_list[i]:
                    if nei not in visited:
                        part = dfs(nei, i, visited, callstack)
                        result = result and part
                    elif nei != parent:
                        return False
                return result
            return True
        
        visited = set()
        result = True
        connected_components = 0
        for i in range(n):
            if i not in visited:
                temp = dfs(i, -1, visited, [])
                connected_components += 1
                if connected_components > 1:
                    return False
                result = result and temp
        
        return result
