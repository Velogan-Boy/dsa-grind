// Last updated: 2/27/2026, 5:03:02 PM
class Solution {
    public int change(int amount, int[] coins) {
        int[][] dp = new int[coins.length][amount + 1];

        for(int[] arr : dp) Arrays.fill(arr,-1);

        return func(coins, coins.length - 1, amount,dp);
    }

    public int func(int[] coins, int index, int amount, int[][] dp){
        if(amount < 0) return 0;
        if(amount == 0) return 1;

        if(index == 0){
            if(amount % coins[index] == 0) return 1;
            else return 0;
        }

        if(dp[index][amount] != -1) return dp[index][amount];
            
        dp[index][amount] = func(coins, index - 1, amount,dp) + func(coins,index, amount - coins[index],dp);

        return dp[index][amount];

    }
}