# Last updated: 5/8/2026, 12:03:59 AM
1class Solution:
2    def findMedianSortedArrays(self, nums1, nums2):
3        n = len(nums1)
4        m = len(nums2)
5        i = 0
6        j = 0
7        m1 = 0
8        m2 = 0
9
10        for count in range(0, (n + m) // 2 + 1):
11            m2 = m1
12            if i < n and j < m:
13                if nums1[i] > nums2[j]:
14                    m1 = nums2[j]
15                    j += 1
16                else:
17                    m1 = nums1[i]
18                    i += 1
19            elif i < n:
20                m1 = nums1[i]
21                i += 1
22            else:
23                m1 = nums2[j]
24                j += 1
25
26        # Check if the sum of n and m is odd.
27        if (n + m) % 2 == 1:
28            return float(m1)
29        else:
30            ans = float(m1) + float(m2)
31            return ans / 2.0