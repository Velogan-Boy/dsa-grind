# Last updated: 6/30/2026, 11:17:47 PM
1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3
4        stack = []
5        nextGreater = {}
6
7        for i in range(len(nums2) - 1, -1, -1):
8
9            while stack and stack[-1] <= nums2[i]:
10                stack.pop()
11
12            nextGreater[nums2[i]] = stack[-1] if stack else -1
13
14            stack.append(nums2[i])
15
16        ans = []
17
18        for num in nums1:
19            ans.append(nextGreater[num])
20
21        return ans