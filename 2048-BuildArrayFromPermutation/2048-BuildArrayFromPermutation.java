// Last updated: 2/28/2026, 4:25:55 PM
class Solution {
    public int[] buildArray(int[] nums) {
        
        int[] ans = new int[nums.length];
        
        for(int i = 0 ; i < nums.length; i++){
             ans[i] = nums[nums[i]];
         } 
        
        return ans;
    }
    
}