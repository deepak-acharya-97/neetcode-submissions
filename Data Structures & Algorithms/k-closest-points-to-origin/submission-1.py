import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def min_heap_approach():
            heap = []
            for x, y in points:
                distance = x**2 + y**2
                heapq.heappush(heap, (distance, x, y))

            result = []
            nonlocal k
            while k > 0:
                dist, x, y = heapq.heappop(heap)
                result.append([x, y])
                k -= 1

            return result

        def max_heap_approach():
            heap = []
            for x, y in points:
                distance = x**2 + y**2
                heapq.heappush(heap, (-distance, x, y))
                if len(heap) > k:
                    heapq.heappop(heap)

            result = []

            while heap:
                dist, x, y = heapq.heappop(heap)
                result.append([x, y])

            return result

        # return min_heap_approach()
        return max_heap_approach()
