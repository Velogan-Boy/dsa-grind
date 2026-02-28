// Last updated: 2/28/2026, 4:27:58 PM
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        
        for(int i = 0; i < nums.length - 1 ; i++){
            if(nums[i] == nums[i+1]) return true;
        }
        
        return false;
    }
}