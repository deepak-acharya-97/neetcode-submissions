"""
https://neetcode.io/problems/network-delay-time
"""
from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_heap = [(0, k)]
        graph = [[] for _ in range(n+1)]

        for s, d, t in times:
            graph[s].append((d, t))

        visited = set()
        result = float("-inf")

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node not in visited:
                visited.add(node)
                result = max(result, time)
                for neighbour, w in graph[node]:
                    heapq.heappush(min_heap, (time+w, neighbour))

        return result if len(visited) == n else -1

