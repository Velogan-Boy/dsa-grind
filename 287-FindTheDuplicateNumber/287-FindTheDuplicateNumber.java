// Last updated: 2/27/2026, 5:19:24 PM
class Solution {
    public int findDuplicate(int[] nums) {
        
        int idx;
        for(int i = 0; i < nums.length; i++){

            idx = Math.abs(nums[i]);

            if(nums[idx] < 0) return idx;

            nums[idx] = -nums[idx];

        }

        return 0;


    }
}