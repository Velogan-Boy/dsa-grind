# Last updated: 7/12/2026, 6:23:42 PM
class Solution:
    def findNSE(self, arr):
        n = len(arr)
        ans = [0] * n
        st = []
        
        for i in range(n - 1, -1, -1):
   
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

