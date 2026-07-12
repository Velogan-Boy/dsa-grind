// Last updated: 7/12/2026, 6:25:49 PM
class Solution {
    public String longestCommonPrefix(String[] strs) {

        if(strs.length == 0) return "";

        StringBuilder str = new StringBuilder(100);

        for(int i=0; i < strs[0].length() ; i++){

            for(int j = 1; j < strs.length; j++){
                if( strs[j].length() == i || strs[j].charAt(i) != strs[0].charAt(i)){
                    return str.toString();
                }
            }

            str.append(strs[0].charAt(i));
        }

        return str.toString();
    }
}