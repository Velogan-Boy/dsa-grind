# Last updated: 5/15/2026, 3:15:37 PM
1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.end = False
5
6class Trie:
7    def __init__(self):
8        self.root = TrieNode()
9
10    def insert(self, word: str) -> None:
11        node = self.root
12
13        for ch in word:
14            if ch not in node.children:
15                node.children[ch] = TrieNode()
16            
17            node = node.children[ch]
18
19        node.end = True
20
21
22    def search(self, word: str) -> bool:
23        node = self.root
24
25        for ch in word:
26            if ch not in node.children: return False
27            else:
28                node = node.children[ch]
29
30        return node.end
31        
32
33    def startsWith(self, prefix: str) -> bool:
34        node = self.root
35
36        for ch in prefix:
37            if ch not in node.children: return False
38            else:
39                node = node.children[ch]
40
41        return True
42        
43
44        
45
46
47# Your Trie object will be instantiated and called as such:
48# obj = Trie()
49# obj.insert(word)
50# param_2 = obj.search(word)
51# param_3 = obj.startsWith(prefix)