# Last updated: 2/27/2026, 5:22:05 PM
class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if not node.children[ord(ch) - ord('a')]:
                node.children[ord(ch) - ord('a')] = TrieNode()
            node = node.children[ord(ch) - ord('a')]

        node.end = True
        

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            if not node.children[ord(ch) - ord('a')]:
                return False
            node = node.children[ord(ch) - ord('a')]
        
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            if not node.children[ord(ch) - ord('a')]:
                return False
            node = node.children[ord(ch) - ord('a')]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)