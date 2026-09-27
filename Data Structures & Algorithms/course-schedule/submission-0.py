from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def approach_1():
            outdegree = [0] * numCourses
            adj = [[] for i in range(numCourses)]
            queue = deque()

            for src, dest in prerequisites:
                outdegree[src] += 1
                adj[src].append(dest)

            for ind, val in enumerate(outdegree):
                if val == 0:
                    queue.append(ind)

            completed_courses = 0
            while queue:
                node = queue.popleft()
                completed_courses += 1
                for n in adj[node]:
                    outdegree[n] -= 1
                    if outdegree[n] == 0:
                        queue.append(n)

            return completed_courses == numCourses

        def approach_2():
            indegree = [0] * numCourses
            graph = [[] for i in range(numCourses)]
            for c1, c2 in prerequisites:
                graph[c2].append(c1)
                indegree[c1] += 1

            queue = deque()

            for i in range(numCourses):
                if indegree[i] == 0:
                    queue.append(i)

            completed = 0

            while queue:
                curr = queue.popleft()
                completed += 1
                for n in graph[curr]:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        queue.append(n)

            return completed == numCourses

        return approach_2()
