# Last updated: 3/23/2026, 4:02:57 PM
1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3
4        n = len(nums2)
5        stack = []
6        ans = [-1] * n
7        hashMap = {}
8
9        for i in range(n - 1, -1, -1):
10            hashMap[nums2[i]] = i
11
12            while stack and stack[-1] <= nums2[i]:
13                stack.pop()
14
15            if stack:
16                ans[i] = stack[-1]
17            
18            stack.append(nums2[i])
19
20        res = []
21        for num in nums1:
22            res.append(ans[hashMap[num]])
23
24        return res
25
26
27
28     