"""
https://neetcode.io/problems/course-schedule-ii
"""
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
            order = []

            while queue:
                curr = queue.popleft()
                order.append(curr)
                completed += 1
                for n in graph[curr]:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        queue.append(n)

            return order if completed == numCourses else []

        return approach_2()