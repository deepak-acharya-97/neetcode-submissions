"""
https://neetcode.io/problems/eating-bananas
"""
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def approach_1():
            speed = 1
            maximum = max(piles)
            while True:
                if speed >= maximum:
                    break
                totalTime = 0
                for pile in piles:
                    totalTime += math.ceil(pile / speed)

                if totalTime <= h:
                    return speed
                speed += 1
            return speed

        def binary_search():
            l, r = 1, max(piles)
            res = r

            while l <= r:
                k = l + (r - l) // 2
                total_time = 0
                for p in piles:
                    total_time += math.ceil(float(p)/k)
                if total_time <= h:
                    res = k
                    r = k - 1
                else:
                    l = k + 1
            return res


        # return approach_1()
        return binary_search()