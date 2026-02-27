// Last updated: 2/27/2026, 5:19:25 PM
class Solution {
    public int lengthOfLIS(int[] nums) {
        
        int[] curr = new int[nums.length + 1];
        int[] next = new int[nums.length + 1];

        for(int index = nums.length - 1; index >= 0 ; index--){
            for(int prev = index - 1; prev >= -1; prev--){

                int len = 0 + next[prev+1];

                if(prev == -1 || nums[index] > nums[prev]){
                    len = Math.max(len, 1 + next[index + 1]);
                }

                curr[prev + 1] = len;
            }

            next = curr;
        }
        
        return next[-1+1];
    }
}

  