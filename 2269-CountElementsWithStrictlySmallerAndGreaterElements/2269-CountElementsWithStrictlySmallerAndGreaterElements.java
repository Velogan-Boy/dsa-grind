// Last updated: 2/28/2026, 4:25:47 PM
class Solution {
    public int countElements(int[] nums) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        //only the min and the max elements satisfy the conditions
        for(int x: nums){
            min = Math.min(x, min);
            max = Math.max(x, max);
        }
        
        if(min == max) return 0; //all the elements in the array are same
        
        int minCount = 0;
        int maxCount = 0;
        
        //all occurances of the maxElement and the minElement must be removed
        for(int x: nums){
            if(x == min) minCount++;
            if(x == max) maxCount++;
        }
        
        return nums.length - minCount - maxCount;
    }
}