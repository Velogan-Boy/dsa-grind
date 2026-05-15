# Last updated: 5/16/2026, 1:48:22 AM
1class Trie:
2    def __init__(self):
3        self.tree = {}   
4        self.bits = 31
5    
6    def add(self,value):
7        node = self.tree
8        for i in range(self.bits,-1,-1):
9            bit = 1 if (1<<i) & value else 0
10            if bit not in node : node[bit] = {}
11            node = node[bit]
12        return 
13
14    # finda max Xor of 'value' with every number present in trie
15    def findMax(self,value):
16        if not self.tree : return -1   
17        node = self.tree
18        maxXor = 0
19        for i in range(self.bits,-1,-1):
20            bit = 1 if (1<<i) & value else 0
21            req = 1-bit
22            if req in node:
23                maxXor |= (1<<i)
24                node = node[req]
25            else:
26                node = node[bit]
27        return maxXor
28
29class Solution:
30    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
31        
32        ln = len(nums)
33        trie = Trie()
34
35        nums.sort()
36        queries = [ [i[0],i[1],ind] for ind,i in enumerate(queries)]
37        queries.sort(key = lambda x : x[1])
38
39        res = [-1] * len(queries)
40        
41        ind = 0
42        for x,maxValue,i in queries:
43            while ind < ln and nums[ind] <= maxValue:
44                trie.add(nums[ind])
45                ind += 1
46            res[i] = trie.findMax(x)
47
48        return res
49