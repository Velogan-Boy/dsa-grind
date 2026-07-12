// Last updated: 7/12/2026, 6:24:18 PM
class Solution {


    public int climbStairs(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp,-1);

        return fn(n,dp);


    }

    public int fn(int index, int[] dp){
        if(index == 0 || index == 1){
            dp[index] = 1;
            return dp[index];
        }

        if(dp[index] == -1){
            dp[index] = fn(index - 1,dp) + fn(index - 2,dp);
        }

        return dp[index];



    }
}