# Sum of Subarray Ranges

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/sum-of-subarray-ranges/submissions/1957098951/
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
            
            while st and arr[st[-1]] >= currEle:
                st.pop()
            
            ans[i] = st[-1] if st else n
            
            st.append(i)
        
        return ans
    
    def findNGE(self, arr):
        n = len(arr)
        ans = [0] * n
        st = []

        for i in range(n - 1, -1, -1):
            
            currEle = arr[i]
            
            while st and arr[st[-1]] <= currEle:
                st.pop()
            
            ans[i] = st[-1] if st else n
            
            st.append(i)
        
        return ans
    
    def findPSEE(self, arr):
        
        n = len(arr)
        ans = [0] * n
        st = []
        
        for i in range(n):
            currEle = arr[i]
            while st and arr[st[-1]] > currEle:
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        
        return ans
    
    def findPGEE(self, arr):
        
        n = len(arr)
        ans = [0] * n
        st = []
        
        for i in range(n):
            currEle = arr[i]
            
            while st and arr[st[-1]] < currEle:
                st.pop()
            
            ans[i] = st[-1] if st else -1
            
            st.append(i)
        
        return ans
    
    def sumSubarrayMins(self, arr):
        
        nse = self.findNSE(arr)
        psee = self.findPSEE(arr)
        
        n = len(arr)
        
        total_sum = 0
        
        for i in range(n):
            
            left = i - psee[i]
            right = nse[i] - i
            
            freq = left * right * 1
            
            val = (freq * arr[i] * 1)
            
            total_sum += val
        
        return total_sum
    
    def sumSubarrayMaxs(self, arr):
        nge = self.findNGE(arr)
        pgee = self.findPGEE(arr)
        
        n = len(arr)
        
        total_sum = 0
        
        for i in range(n):
            
            left = i - pgee[i]
            
            right = nge[i] - i
            
            freq = left * right * 1
            val = (freq * arr[i] * 1)
            
            total_sum += val
        
        return total_sum
    
    def subArrayRanges(self, arr):
        return (self.sumSubarrayMaxs(arr) - 
                self.sumSubarrayMins(arr))


```

---
*Generated automatically by LeetFeedback Extension*
