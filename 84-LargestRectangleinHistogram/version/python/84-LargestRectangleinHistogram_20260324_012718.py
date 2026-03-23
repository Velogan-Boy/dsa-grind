# Last updated: 3/24/2026, 1:27:18 AM
1class Solution:
2    def findNSE(self, arr):
3        n = len(arr)
4        ans = [0] * n
5        st = []
6        
7        for i in range(n - 1, -1, -1):
8            currEle = arr[i]
9            while st and arr[st[-1]] >= arr[i]:
10                st.pop()
11            
12            ans[i] = st[-1] if st else n
13            
14            st.append(i)
15        
16        return ans
17    
18    def findPSE(self, arr):
19        n = len(arr)
20        ans = [0] * n
21        st = []
22        for i in range(n):
23            currEle = arr[i]
24            while st and arr[st[-1]] >= arr[i]:
25                st.pop()
26            ans[i] = st[-1] if st else -1
27            
28            st.append(i)
29        
30        return ans
31    
32    def largestRectangleArea(self, heights):
33        
34        nse = self.findNSE(heights)
35        pse = self.findPSE(heights)
36        
37        largestArea = 0
38        area = 0
39        
40        for i in range(len(heights)):
41            area = heights[i] * (nse[i]-pse[i]-1)
42            largestArea = max(largestArea, area)
43        
44        return largestArea
45
46