// Last updated: 2/27/2026, 5:18:52 PM
   class Solution {
    public int minimumDifference(int[] nums, int k) {
        int n = nums.length;
        Arrays.sort(nums);
        int res = 9999999;
        for(int i=0; i + k<=n; i++){
            res = Math.min(res, nums[k+i-1] - nums[i]);
        }
        
        return res;
    }
}