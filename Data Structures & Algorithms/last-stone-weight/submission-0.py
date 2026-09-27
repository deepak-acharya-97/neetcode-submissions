from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [stone*-1 for stone in stones]
        heapq.heapify(max_heap)

        while max_heap:
            if len(max_heap) == 1:
                break
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if x != y:
                heapq.heappush(max_heap, -(-x + y))

        if not max_heap:
            return 0
        return -max_heap[0]
