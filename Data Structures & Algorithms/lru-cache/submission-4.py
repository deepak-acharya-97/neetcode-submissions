"""
https://neetcode.io/problems/lru-cache
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                popped = self.cache.pop(i)
                self.cache.append(popped)
                return v
        return -1

    def put(self, key: int, value: int) -> None:
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                popped = self.cache.pop(i)
                self.cache.append((popped[0], value))
                return

        if len(self.cache) == self.capacity:
            self.cache.pop(0)

        self.cache.append((key, value))


