# Last updated: 7/12/2026, 6:17:59 PM
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
    
    def findPSEE(self, arr):
        n = len(arr)
        ans = [0] * n
        st = []
        
        for i in range(n):
            currEle = arr[i]
            
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            
            ans[i] = st[-1] if st else -1
            
            st.append(i)
        
        return ans

    def sumSubarrayMins(self, arr: List[int]) -> int:

        nse = self.findNSE(arr)
        psee = self.findPSEE(arr)
        
        n = len(arr)
        
        mod = int(1e9 + 7) 
        
        total_sum = 0
        
        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i
            
            freq = left * right * 1
            val = (freq * arr[i]) % mod
            
            total_sum = (total_sum + val) % mod
        
        return total_sum


        
        