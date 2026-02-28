// Last updated: 2/28/2026, 4:26:03 PM
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
     
        int[] res = new int[nums.length];
        
        for(int i=0; i<nums.length ; i++){
            for(int j = 0; j < nums.length ; j++){
                if(nums[j] < nums[i]){
                   res[i]++; 
                }
            }
        }
        
        return res;
    }
}