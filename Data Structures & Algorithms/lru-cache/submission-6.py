"""
https://neetcode.io/problems/lru-cache
"""
from typing import Optional, Union


# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = []
#
#     def get(self, key: int) -> int:
#         for i, (k, v) in enumerate(self.cache):
#             if k == key:
#                 popped = self.cache.pop(i)
#                 self.cache.append(popped)
#                 return v
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         for i, (k, v) in enumerate(self.cache):
#             if k == key:
#                 popped = self.cache.pop(i)
#                 self.cache.append((popped[0], value))
#                 return
#
#         if len(self.cache) == self.capacity:
#             self.cache.pop(0)
#
#         self.cache.append((key, value))

class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev: Optional[LinkedListNode] = None
        self.next: Union[LinkedListNode, None] = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = LinkedListNode(0, 0)
        self.right = LinkedListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Optional[LinkedListNode]):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add(self, node: Optional[LinkedListNode]):
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache.get(key)
            self.remove(node)
            self.add(node)
            return node.value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            self.remove(node)
            self.add(node)
            return

        if len(self.cache) == self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)

        node = LinkedListNode(key, value)
        self.add(node)
        self.cache[key] = node

