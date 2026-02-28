// Last updated: 2/28/2026, 4:25:46 PM
class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n * 2];
        int i;
        
        for( i = 0; i < n ; i++){
            ans[i] = nums[i];
        }
        
        for(i = 0; i < nums.length ; i++){
            ans[n + i] = nums[i];
        }
        
        return ans;
    }
}