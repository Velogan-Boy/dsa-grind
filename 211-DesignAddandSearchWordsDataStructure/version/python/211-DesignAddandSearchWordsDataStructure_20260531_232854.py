# Last updated: 5/31/2026, 11:28:54 PM
1class TrieNode:
2    def __init__(self):
3        self.children = [None] * 26
4        self.isEnd = False
5
6
7class WordDictionary:
8
9    def __init__(self):
10        self.root = TrieNode()
11
12    def addWord(self, word: str) -> None:
13        node = self.root
14
15        for ch in word:
16            idx = ord(ch) - ord('a')
17
18            if node.children[idx] is None:
19                node.children[idx] = TrieNode()
20
21            node = node.children[idx]
22
23        node.isEnd = True
24
25    def search(self, word: str) -> bool:
26
27        def dfs(i, node):
28            if not node:
29                return False
30
31            if i == len(word):
32                return node.isEnd
33
34            ch = word[i]
35
36            if ch == '.':
37                for child in node.children:
38                    if child and dfs(i + 1, child):
39                        return True
40                return False
41
42            idx = ord(ch) - ord('a')
43            return dfs(i + 1, node.children[idx])
44
45        return dfs(0, self.root)