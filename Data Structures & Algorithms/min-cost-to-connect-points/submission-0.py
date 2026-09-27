"""
https://neetcode.io/problems/min-cost-to-connect-points
"""
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        graph = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((distance, j))
                graph[j].append((distance, i))

        result = 0
        minHeap = [(0, 0)]
        visited = set()

        while len(visited) < n:
            distance, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            result += distance
            for n_dist, n_node in graph[node]:
                if n_node not in visited:
                    heapq.heappush(minHeap, (n_dist, n_node))

        return result

