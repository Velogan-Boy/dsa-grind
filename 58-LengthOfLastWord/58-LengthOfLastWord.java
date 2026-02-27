// Last updated: 2/27/2026, 9:37:24 PM
class Solution {
    public int lengthOfLastWord(String s) {
     
        int flag = 0;
        int n = 0;
        
        for(int i = s.length() - 1; i >=0; i-- ){
            if(s.charAt(i) == ' ' && flag == 0){
                continue;
            }
            
            if(s.charAt(i) == ' ' && flag == 1){
                break;
            }
            
            flag = 1;
            n++;
        }
        
        return n;
    }
}