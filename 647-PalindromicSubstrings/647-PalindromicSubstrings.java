// Last updated: 2/28/2026, 4:27:11 PM
class Solution {
    public int countSubstrings(String s) {

        if(s == null || s.length() == 0) return 0;

        if(s.length() == 1) return 1;

        int count = 0;

        for(int i = 0; i < s.length(); i++){
            count += expandFromCenter(s, i, i);
            count += expandFromCenter(s, i,i+1);
        }

        return count; 
        
    }

    public int expandFromCenter(String s, int left, int right){

        if(s == null || s.length() == 0) return 0;

        int count = 0;
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            left--;
            right++;
            count++;
        }

        return count;

    }
}