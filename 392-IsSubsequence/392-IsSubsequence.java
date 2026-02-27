// Last updated: 2/27/2026, 5:03:06 PM
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