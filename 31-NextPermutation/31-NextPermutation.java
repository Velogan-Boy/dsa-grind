// Last updated: 7/12/2026, 6:25:16 PM
class Solution {
    public void nextPermutation(int[] nums) {
        
        if(nums.length == 0 || nums.length == 1 || nums == null) return;

        int index = -1;
        int n = nums.length;

        for(int i = n - 2; i >= 0 ; i--){
            if(nums[i] < nums[i + 1]) {
                index = i;
                break;
            }
        }

        System.out.println(index);

        if(index == -1) {
            int i = 0;
            int j = n - 1;

            while(i <= j){
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j--;
            }
            return;
        }

        for(int i = n - 1; i > index; i--){
            if(nums[i] > nums[index]){
                int temp = nums[index];
                nums[index] = nums[i];
                nums[i] = temp;
                break;
            }
        }

        Arrays.sort(nums, index + 1, n);


    }
}