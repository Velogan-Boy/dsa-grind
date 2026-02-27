// Last updated: 2/27/2026, 5:22:15 PM
class Solution {
    public int longestConsecutive(int[] nums) {

        if(nums.length == 0) return 0;

        HashSet<Integer> set = new HashSet<>();

        for(int i : nums) set.add(i);

        int max = Integer.MIN_VALUE;

        for(int i = 0; i < nums.length; i++){

            if(!set.contains(nums[i] - 1)){
                int curr = nums[i];
                int currLength = 0;
                while(set.contains(curr)) {
                     curr++;
                     currLength++;
                }

                max = Math.max(currLength, max);
            }


        }

        return max;

    }
}