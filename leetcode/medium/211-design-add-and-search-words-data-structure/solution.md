# Design Add and Search Words Data Structure

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/2018400592/
- **Date:** 2026-05-31

## Solution

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if node.children[idx] is None:
                node.children[idx] = TrieNode()

            node = node.children[idx]

        node.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if not node:
                return False

            if i == len(word):
                return node.isEnd

            ch = word[i]

            if ch == '.':
                for child in node.children:
                    if child and dfs(i + 1, child):
                        return True
                return False

            idx = ord(ch) - ord('a')
            return dfs(i + 1, node.children[idx])

        return dfs(0, self.root)
```

---
*Generated automatically by LeetFeedback Extension*
