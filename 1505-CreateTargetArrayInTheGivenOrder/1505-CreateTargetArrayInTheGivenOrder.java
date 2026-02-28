// Last updated: 2/28/2026, 4:26:05 PM
class Solution {
      public int[] createTargetArray(int[] nums, int[] index) {
        int[] target = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            int temp = target[index[i]];
            target[index[i]] = nums[i];
            swap(target, temp , index[i]);
        }
        return target;
    }
    void swap(int[] target, int temp, int i){
        int temp2 = 0;
        while(i<target.length-1){
            temp2 = target[i+1];
            target[i+1] = temp;
            temp = temp2;
            i += 1;
        }
        return;
    }
}