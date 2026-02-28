// Last updated: 2/28/2026, 4:27:41 PM
class Solution {
    public void moveZeroes(int[] nums) {


        int zeroCount = 0;
        for(int x = 0; x < nums.length; x++){
            if(nums[x] == 0 ) zeroCount++;
        }

        if(zeroCount == 0) return;

        int nonzeroCount = nums.length - zeroCount;

        int i = 0;
        int j = 0;

        while(j < nums.length && i < nonzeroCount){
            if(nums[j] != 0){
                nums[i] = nums[j];
                i++;
            }
            j++;
        }

        while(i < nums.length){
            nums[i] = 0;
            i++;
        }


        
    }
}