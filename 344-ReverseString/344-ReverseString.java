// Last updated: 2/28/2026, 4:27:34 PM
class Solution {
    public void reverseString(char[] s) {

        solve(s,0,s.length - 1);
        
    }

    public void solve(char[] s, int i , int j){
        if(i >= j) return;

        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;

        solve(s,++i,--j); 
    }
}