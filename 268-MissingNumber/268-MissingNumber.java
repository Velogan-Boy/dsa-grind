// Last updated: 2/28/2026, 4:27:43 PM
class Solution {
    public int missingNumber(int[] nums) {
        cyclicSort(nums);
        int i = 0;
        for( i = 0; i < nums.length; i++){
            if(nums[i] != i) return i;
        }
             
                
        return i;
    }
    
    void cyclicSort(int[] nums){
         int i = 0;
        
        while(i < nums.length){
            
            if(nums[i] < nums.length && nums[i] != nums[nums[i]]){
                swap(nums,i,nums[i]);
            }else i++;
        }
       
    }
    
    void swap(int arr[], int i,int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}