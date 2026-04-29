# Is Subsequence

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/is-subsequence/submissions/1991266472/
- **Date:** 2026-04-29

## Solution

```java
class Solution {
    public boolean isSubsequence(String s, String t) {
       
        int s_len = s.length();
        int t_len = t.length();
        
        if(s_len == 0) return true;
        if(s_len > t_len) return false;
        
        int i = 0;
        
        for(int j = 0; j < t_len; j++){
            if(s.charAt(i) == t.charAt(j)){
                i++;
                if(i == s_len) return true;
                continue;
            }
        }
        
        
        
        return false;
        
        
    }
}
```

---
*Generated automatically by LeetFeedback Extension*
