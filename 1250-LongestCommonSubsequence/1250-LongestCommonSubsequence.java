// Last updated: 2/28/2026, 4:26:17 PM
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {

        int[][] dp = new int[text1.length()][text2.length()];

        for(int[] arr : dp){
            Arrays.fill(arr,-1);
        }

        return func(text1,text2,text1.length()-1,text2.length()-1,dp);
    }

    public int func(String text1, String text2 , int index1, int index2, int[][] dp){

        if(index1 < 0 || index2 < 0) return 0;

        if(dp[index1][index2] != -1) return dp[index1][index2];

        if(text1.charAt(index1) == text2.charAt(index2))
            dp[index1][index2] =  1 + func(text1,text2,index1 - 1,index2 - 1,dp);
        else
            dp[index1][index2] = 0 + Math.max(func(text1,text2,index1-1,index2,dp), func(text1,text2,index1,index2-1,dp));

        return dp[index1][index2];
    }
}