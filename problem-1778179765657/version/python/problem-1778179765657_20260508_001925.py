# Last updated: 5/8/2026, 12:19:25 AM
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
15            mid1 = (low + high) // 2 # Calculate mid index for nums1
16            mid2 = left - mid1 # Calculate mid index for nums2
17            
18            l1 = float('-inf')
19            l2 = float('-inf')
20            r1 = float('inf')
21            r2 = float('inf')
22            
23            # Determine values of l1, l2, r1, and r2
24            if mid1 < n1:
25                r1 = nums1[mid1]
26            if mid2 < n2:
27                r2 = nums2[mid2]
28            if mid1 - 1 >= 0:
29                l1 = nums1[mid1 - 1]
30            if mid2 - 1 >= 0:
31                l2 = nums2[mid2 - 1]
32            
33            if l1 <= r2 and l2 <= r1:
34                # The partition is correct, we found the median
35                if n % 2 == 1:
36                    return max(l1, l2)
37                else:
38                    return (max(l1, l2) + min(r1, r2)) / 2.0
39            elif l1 > r2:
40                # Move towards the left side of nums1
41                high = mid1 - 1
42            else:
43                # Move towards the right side of nums1
44                low = mid1 + 1
45        
46        return 0 # If the code reaches here, the input arrays were not sorted.