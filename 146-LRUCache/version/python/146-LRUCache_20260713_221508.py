# Last updated: 7/13/2026, 10:15:08 PM
1class Node:
2    def __init__(self, key, value):
3        self.key = key
4        self.value = value
5        self.prev = None
6        self.next = None
7
8
9class LRUCache:
10
11    def __init__(self, capacity: int):
12        self.capacity = capacity
13        self.hm = {}
14
15        self.head = Node(0, 0)
16        self.tail = Node(0, 0)
17
18        self.head.next = self.tail
19        self.tail.prev = self.head
20
21    def remove(self, node):
22        prev = node.prev
23        nxt = node.next
24
25        prev.next = nxt
26        nxt.prev = prev
27
28    def insert_front(self, node):
29        first = self.head.next
30
31        self.head.next = node
32        node.prev = self.head
33
34        node.next = first
35        first.prev = node
36
37    def get(self, key: int) -> int:
38
39        if key not in self.hm:
40            return -1
41
42        node = self.hm[key]
43
44        self.remove(node)
45        self.insert_front(node)
46
47        return node.value
48
49    def put(self, key: int, value: int) -> None:
50
51        if key in self.hm:
52            node = self.hm[key]
53            node.value = value
54
55            self.remove(node)
56            self.insert_front(node)
57            return
58
59        if len(self.hm) == self.capacity:
60            lru = self.tail.prev
61
62            self.remove(lru)
63            del self.hm[lru.key]
64
65        node = Node(key, value)
66
67        self.insert_front(node)
68        self.hm[key] = node