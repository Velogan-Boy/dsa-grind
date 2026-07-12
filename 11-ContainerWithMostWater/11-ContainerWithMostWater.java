// Last updated: 7/12/2026, 6:26:06 PM
class Solution {
    public int maxArea(int[] height) {

        int maxArea = Integer.MIN_VALUE;

        int left = 0;
        int right = height.length - 1;

        while(left < right){
            int area = (right - left) * Math.min(height[left],height[right]);
            maxArea = Math.max(area,maxArea);

            if(height[left] < height[right]) left++;
            else right--;
        }

        return maxArea;
    }
}