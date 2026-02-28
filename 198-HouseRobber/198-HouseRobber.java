// Last updated: 2/28/2026, 4:28:10 PM
class Solution {
    public int rob(int[] nums) {

        int[] dp = new int[nums.length];

        Arrays.fill(dp,-1);

        return func(nums,nums.length - 1,dp);
        
    }

    public int func(int[] nums, int index, int[] dp){

        if(index < 0) return 0;

        if(index == 0) return nums[index];

        if(dp[index] != -1) return dp[index];

        int rob = nums[index] + func(nums,index - 2,dp);
        int notRob = 0 + func(nums,index - 1,dp);

        dp[index] =  Math.max(rob,notRob);

        return dp[index];

    }
}