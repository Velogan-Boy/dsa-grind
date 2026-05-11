# Last updated: 5/11/2026, 2:27:28 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        
4        element1, element2 = 0, 1
5        count1, count2 = 0, 0 
6        n = len(nums)
7
8        for num in nums:
9            if element1 == num:
10                count1+= 1
11            elif element2 == num:
12                count2+=1
13            elif count1 == 0:
14                element1 = num
15                count1 = 1
16            elif count2 == 0:
17                element2 = num
18                count2 = 1
19            else:
20                count1-=1
21                count2-=1
22
23        count1 = 0
24        count2 = 0
25        for num in nums:
26            if num == element1:
27                count1+=1
28            elif num == element2:
29                count2+=1
30
31        ans = []
32        if count1 > n // 3:
33            ans.append(element1)
34        
35        if count2 > n // 3:
36            ans.append(element2)
37
38        return ans
39
40
41            
42
43
44
45        