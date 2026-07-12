// Last updated: 7/12/2026, 6:25:28 PM
class Solution {
    public int removeDuplicates(int[] nums) {

        if(nums.length == 0 || nums.length == 1) return nums.length;
        
        int i = 1;
        int j = 1;

        while(j < nums.length){
            if(nums[j] != nums[j - 1]){
                nums[i] = nums[j];
                i++; 
            }
            j++;
        }

        return i;

        
    }
}