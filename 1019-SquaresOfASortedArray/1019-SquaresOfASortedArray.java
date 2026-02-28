// Last updated: 2/28/2026, 4:26:22 PM
class Solution {
    public int[] sortedSquares(int[] nums) {
        
        int base = nums.length - 1;

        for(int i = 0; i < nums.length - 1; i++){
            if(Math.abs(nums[i]) < Math.abs(nums[i+1])) {
                base = i;
                break;
            }

        }

        int[] sol = new int[nums.length];

        int i = base - 1;
        int j = base + 1;
        int k = 0;

        sol[k++] = nums[base] * nums[base];

        while(i >= 0 && j < nums.length){
            if(Math.abs(nums[i]) < Math.abs(nums[j])){
                sol[k++] = nums[i] * nums[i];
                i--;
            }else{
                sol[k++] = nums[j] * nums[j];
                j++;
            }
        }

        while(i >= 0){
            sol[k++] = nums[i] * nums[i];
            i--;
        }

        while(j < nums.length){
            sol[k++] = nums[j] * nums[j];
            j++;
        }

        
        return sol;

       

    }
}