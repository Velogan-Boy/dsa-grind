# Last updated: 3/24/2026, 12:58:56 AM
1class Solution:
2    def findNSE(self, arr):
3        
4        n = len(arr)
5        ans = [0] * n
6        
7        st = []
8        
9        for i in range(n - 1, -1, -1):
10            currEle = arr[i]
11            
12            while st and arr[st[-1]] >= currEle:
13                st.pop()
14            
15            ans[i] = st[-1] if st else n
16            
17            st.append(i)
18        
19        return ans
20    
21    def findNGE(self, arr):
22        n = len(arr)
23        ans = [0] * n
24        st = []
25
26        for i in range(n - 1, -1, -1):
27            
28            currEle = arr[i]
29            
30            while st and arr[st[-1]] <= currEle:
31                st.pop()
32            
33            ans[i] = st[-1] if st else n
34            
35            st.append(i)
36        
37        return ans
38    
39    def findPSEE(self, arr):
40        
41        n = len(arr)
42        ans = [0] * n
43        st = []
44        
45        for i in range(n):
46            currEle = arr[i]
47            while st and arr[st[-1]] > currEle:
48                st.pop()
49            ans[i] = st[-1] if st else -1
50            st.append(i)
51        
52        return ans
53    
54    def findPGEE(self, arr):
55        
56        n = len(arr)
57        ans = [0] * n
58        st = []
59        
60        for i in range(n):
61            currEle = arr[i]
62            
63            while st and arr[st[-1]] < currEle:
64                st.pop()
65            
66            ans[i] = st[-1] if st else -1
67            
68            st.append(i)
69        
70        return ans
71    
72    def sumSubarrayMins(self, arr):
73        
74        nse = self.findNSE(arr)
75        psee = self.findPSEE(arr)
76        
77        n = len(arr)
78        
79        total_sum = 0
80        
81        for i in range(n):
82            
83            left = i - psee[i]
84            right = nse[i] - i
85            
86            freq = left * right * 1
87            
88            val = (freq * arr[i] * 1)
89            
90            total_sum += val
91        
92        return total_sum
93    
94    def sumSubarrayMaxs(self, arr):
95        nge = self.findNGE(arr)
96        pgee = self.findPGEE(arr)
97        
98        n = len(arr)
99        
100        total_sum = 0
101        
102        for i in range(n):
103            
104            left = i - pgee[i]
105            
106            right = nge[i] - i
107            
108            freq = left * right * 1
109            val = (freq * arr[i] * 1)
110            
111            total_sum += val
112        
113        return total_sum
114    
115    def subArrayRanges(self, arr):
116        return (self.sumSubarrayMaxs(arr) - 
117                self.sumSubarrayMins(arr))
118
119