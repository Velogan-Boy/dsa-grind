// Last updated: 2/28/2026, 4:25:59 PM
class Solution {
    public int[] runningSum(int[] nums) {
        
        int count = 0;
        
        while(count != nums.length){
            if(count != 0){
                nums[count] = nums[count] + nums[count - 1];
            }
            
            count++;
        }
        
        
        return nums;
    }
}