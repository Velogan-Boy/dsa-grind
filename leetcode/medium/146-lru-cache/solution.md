# LRU Cache

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/lru-cache/submissions/2066401834/
- **Date:** 2026-07-13

## Solution

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert_front(self, node):
        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node

    def get(self, key: int) -> int:

        if key not in self.hm:
            return -1

        node = self.hm[key]

        self.remove(node)
        self.insert_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.hm:
            node = self.hm[key]
            node.value = value

            self.remove(node)
            self.insert_front(node)
            return

        if len(self.hm) == self.capacity:
            lru = self.tail.prev

            self.remove(lru)
            del self.hm[lru.key]

        node = Node(key, value)

        self.insert_front(node)
        self.hm[key] = node
```

---
*Generated automatically by LeetFeedback Extension*
