// Last updated: 2/28/2026, 4:27:33 PM
class Solution {
    public int coinChange(int[] coins, int amount) {

            int[][] dp = new int[coins.length][amount + 1];

            for(int[] arr : dp){
                Arrays.fill(arr,-1);
            }

            int ans = func(coins,coins.length - 1,amount, dp);
        

            if(ans == Integer.MAX_VALUE - 1) return -1;

            return ans;
    }   

    public int func(int[] coins, int index, int amount, int[][] dp){

        if(amount < 0) return Integer.MAX_VALUE - 1;

        if(index == 0) {
            if(amount % coins[0] == 0) return amount / coins[0];
            else return Integer.MAX_VALUE - 1; 
        } 

        if(dp[index][amount] != -1) return dp[index][amount];

        int notPick = 0 + func(coins,index - 1, amount,dp);
        int pick = Integer.MAX_VALUE - 1;

        if(amount >= coins[index])
            pick = 1 + func(coins,index,amount - coins[index],dp);

        dp[index][amount] =  Math.min(pick,notPick);

        return dp[index][amount];
    }
}