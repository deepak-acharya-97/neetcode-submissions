class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def bfs():
            indegree = [0]*numCourses
            graph = defaultdict(list)
            for a, b in prerequisites:
                #b is prereque of a
                graph[b].append(a)
                indegree[a] += 1
            print(indegree)
            q = deque()
            visited = set()
            for ind, val in enumerate(indegree):
                if val == 0:
                    q.append(ind)
                    visited.add(ind)
            completed = 0
            order = []
            while q:
                curr = q.popleft()
                order.append(curr)
                completed += 1
                for adj in graph[curr]:
                    indegree[adj] -= 1
                    if indegree[adj] == 0:
                        q.append(adj)
                        visited.add(adj)
            return completed == numCourses

        return bfs()

        