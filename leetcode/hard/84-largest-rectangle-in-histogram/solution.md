# Largest Rectangle in Histogram

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/1957117099/
- **Date:** 2026-03-23

## Solution

```python
class Solution:
    def findNSE(self, arr):
        n = len(arr)
        ans = [0] * n
        st = []
        
        for i in range(n - 1, -1, -1):
            currEle = arr[i]
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            
            ans[i] = st[-1] if st else n
            
            st.append(i)
        
        return ans
    
    def findPSE(self, arr):
        n = len(arr)
        ans = [0] * n
        st = []
        for i in range(n):
            currEle = arr[i]
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            ans[i] = st[-1] if st else -1
            
            st.append(i)
        
        return ans
    
    def largestRectangleArea(self, heights):
        
        nse = self.findNSE(heights)
        pse = self.findPSE(heights)
        
        largestArea = 0
        area = 0
        
        for i in range(len(heights)):
            area = heights[i] * (nse[i]-pse[i]-1)
            largestArea = max(largestArea, area)
        
        return largestArea


```

---
*Generated automatically by LeetFeedback Extension*
