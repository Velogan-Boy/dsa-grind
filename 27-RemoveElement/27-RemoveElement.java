// Last updated: 7/12/2026, 6:25:17 PM
class Solution {
    public int removeElement(int[] nums, int val) {

        if(nums.length == 0) return 0;

        int flag = 0;

        for(int x = 0; x < nums.length; x++){
            if(nums[x] != val) flag = 1;
        }

        if(flag == 0) return 0;

                       
        int k = 0, i = 0, j = 0;

        for( i = nums.length - 1; i >= 0 ; i--){
            if(nums[i] == val) {
                k++;
                continue;
            }
           for( j = 0; j < i; j++){
                if(nums[j] == val){
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp; 
                    k++;
                    break;
                }
            }
            if(i == j) break;

        }


        return nums.length - k;


            


    }

   
}