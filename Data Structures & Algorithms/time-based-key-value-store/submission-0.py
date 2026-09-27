"""
https://neetcode.io/problems/time-based-key-value-store
"""
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.map[key]) == 0:
            return ""
        elements = self.map.get(key)
        print(elements)
        l, r = 0, len(elements) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2
            if elements[m][0] <= timestamp:
                res = elements[m][1]
                l = m + 1
            else:
                r = m - 1
        return res


