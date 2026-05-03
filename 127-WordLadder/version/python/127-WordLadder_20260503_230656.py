# Last updated: 5/3/2026, 11:06:56 PM
1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3        queue = deque([beginWord])
4        visited = set([beginWord])
5        wordList = set(wordList)
6        
7        changes = 1
8        
9        alph = "abcdefghijklmnopqrstuvwxyz"
10        
11        
12        if endWord not in wordList:
13            return 0
14        
15        while queue:
16            for l in range(len(queue)):
17                curr_word = queue.popleft()
18                if curr_word == endWord:
19                    return changes
20
21                for i in range(len(curr_word)):
22                    prefix, suffix = curr_word[:i], curr_word[i+1:]
23                    for al in alph:
24                        w = prefix + al + suffix
25                        if w in wordList and w not in visited:
26                            queue.append(w)
27                            visited.add(w)
28            changes += 1
29            
30        return 0
31                  