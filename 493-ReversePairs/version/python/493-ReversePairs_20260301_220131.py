# Last updated: 3/1/2026, 10:01:31 PM
1class Solution:
2    def reversePairs(self, nums):
3        return self.merge_sort(nums, 0, len(nums) - 1)
4
5    def merge_sort(self, nums, start, end):
6        if start >= end:
7            return 0
8
9        mid = (start + end) // 2
10        count = self.merge_sort(nums, start, mid)
11        count += self.merge_sort(nums, mid + 1, end)
12        count += self.count_pairs(nums, start, mid, end)
13        self.merge(nums, start, mid, end)
14        return count
15
16    def count_pairs(self, nums, start, mid, end):
17        count = 0
18        j = mid + 1
19        for i in range(start, mid + 1):
20            while j <= end and nums[i] > 2 * nums[j]:
21                j += 1
22            count += j - (mid + 1)
23        return count
24
25    def merge(self, nums, start, mid, end):
26        temp = []
27        left, right = start, mid + 1
28
29        while left <= mid and right <= end:
30            if nums[left] <= nums[right]:
31                temp.append(nums[left])
32                left += 1
33            else:
34                temp.append(nums[right])
35                right += 1
36
37        while left <= mid:
38            temp.append(nums[left])
39            left += 1
40        while right <= end:
41            temp.append(nums[right])
42            right += 1
43
44        for i in range(len(temp)):
45            nums[start + i] = temp[i]