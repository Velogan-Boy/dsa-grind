// Last updated: 2/28/2026, 4:25:48 PM
class Solution {
    public boolean checkIfPangram(String sentence) {
        for(char c  = 'a'; c <= 'z'; c++)
            if(!sentence.contains(""+c))return false;
        return true;
    }
}