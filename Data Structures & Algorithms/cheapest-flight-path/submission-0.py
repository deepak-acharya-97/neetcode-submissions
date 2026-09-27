"""
https://neetcode.io/problems/cheapest-flight-path
"""
from collections import deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}

        for s, d, p in flights:
            graph[s].append((p, d))

        distance = [float("inf") for _ in range(n)]
        distance[src] = 0

        queue = deque([(0, src, 0)])

        while queue:
            cost, node, stops = queue.popleft()

            if stops > k:
                continue

            for curr_price, neigbour in graph[node]:
                if cost + curr_price < distance[neigbour]:
                    distance[neigbour] = cost + curr_price
                    queue.append((cost + curr_price, neigbour, stops+1))

        return distance[dst] if distance[dst] != float("inf") else -1

