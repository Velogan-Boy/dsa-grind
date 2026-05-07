# Last updated: 5/8/2026, 12:26:47 AM
1class Solution:
2    def findMedianSortedArrays(self, nums1, nums2):
3        n1 = len(nums1)
4        n2 = len(nums2)
5        
6        if n1 > n2:
7            return self.findMedianSortedArrays(nums2, nums1)
8        
9        n = n1 + n2
10        left = (n1 + n2 + 1) // 2 
11        low = 0
12        high = n1
13        
14        while low <= high:
15            mid1 = (low + high) // 2 
16            mid2 = left - mid1 
17            
18            l1 = float('-inf')
19            l2 = float('-inf')
20            r1 = float('inf')
21            r2 = float('inf')
22            
23            if mid1 < n1:
24                r1 = nums1[mid1]
25            if mid2 < n2:
26                r2 = nums2[mid2]
27            if mid1 - 1 >= 0:
28                l1 = nums1[mid1 - 1]
29            if mid2 - 1 >= 0:
30                l2 = nums2[mid2 - 1]
31            
32            if l1 <= r2 and l2 <= r1:
33                if n % 2 == 1:
34                    return max(l1, l2)
35                else:
36                    return (max(l1, l2) + min(r1, r2)) / 2.0
37            elif l1 > r2:
38                high = mid1 - 1
39            else:
40                low = mid1 + 1
41        
42        return 0 