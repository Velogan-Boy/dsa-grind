# Last updated: 3/24/2026, 1:09:07 AM
1class Solution:
2    def removeKdigits(self, nums: str, k: int) -> str:
3        st = []
4        
5        for digit in nums:
6            while st and k > 0 and st[-1] > digit:
7                st.pop() 
8                k -= 1 
9            
10            st.append(digit)
11        
12        while st and k > 0:
13            st.pop() 
14            k -= 1 
15        
16        if not st:
17            return "0"
18        
19        res = ""
20        
21        while st:
22            res += st.pop()
23        
24        res = res.rstrip('0')
25        
26        res = res[::-1]
27        
28        if not res:
29            return "0"
30        
31        return res
32