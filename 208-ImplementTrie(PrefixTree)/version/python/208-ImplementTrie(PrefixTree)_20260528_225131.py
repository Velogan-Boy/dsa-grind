# Last updated: 5/28/2026, 10:51:31 PM
1class TrieNode:
2    def __init__(self):
3        self.hashMap = {}
4        self.isEnd = False
5
6
7
8class Trie:
9    def __init__(self):
10        self.root = TrieNode()
11        
12
13    def insert(self, word: str) -> None:
14
15        node = self.root
16
17        for ch in word:
18            if ch not in node.hashMap:
19                node.hashMap[ch] = TrieNode()
20
21            node = node.hashMap[ch]
22        
23        node.isEnd = True 
24
25    def search(self, word: str) -> bool:
26        node = self.root
27
28        for ch in word:
29            if ch not in node.hashMap: return False
30
31            node = node.hashMap[ch]
32
33        return node.isEnd
34
35
36    def startsWith(self, prefix: str) -> bool:
37        node = self.root
38
39        for ch in prefix:
40            if ch not in node.hashMap: return False
41
42            node = node.hashMap[ch]
43
44        return True
45        
46
47
48# Your Trie object will be instantiated and called as such:
49# obj = Trie()
50# obj.insert(word)
51# param_2 = obj.search(word)
52# param_3 = obj.startsWith(prefix)