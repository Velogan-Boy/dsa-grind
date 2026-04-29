// Last updated: 4/29/2026, 11:57:23 PM
1class Solution {
2    public boolean isSubsequence(String s, String t) {
3       
4        int s_len = s.length();
5        int t_len = t.length();
6        
7        if(s_len == 0) return true;
8        if(s_len > t_len) return false;
9        
10        int i = 0;
11        
12        for(int j = 0; j < t_len; j++){
13            if(s.charAt(i) == t.charAt(j)){
14                i++;
15                if(i == s_len) return true;
16                continue;
17            }
18        }
19        
20        
21        
22        return false;
23        
24        
25    }
26}