// Last updated: 2/27/2026, 5:21:35 PM
/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        
        // first find peak element
        int peak = findPeakElement(mountainArr);
        
        int ans = binarySearch(mountainArr, target, 0 ,peak);
        
        if(ans == -1){
         ans = binarySearch(mountainArr, target, peak + 1 ,mountainArr.length() - 1);
        }
        
        return ans;
       

    }
    
     int findPeakElement(MountainArray nums) {
        int left = 0, right = nums.length() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums.get(mid) > nums.get(mid + 1)) right = mid;
            else left = mid + 1;
        }
        return left;
    }
    
    int binarySearch(MountainArray nums, int target, int start, int end){
                
        int s = start;
        int e = end;
        
        boolean isAsc = nums.get(start) < nums.get(end);
        
        while(s <= e){
            int mid = s + (e-s)/2;
            
            if(isAsc){
                if(nums.get(mid) > target) e = mid - 1;
                else if(nums.get(mid) < target) s = mid + 1;
                else return mid;
            }else{
                if(nums.get(mid) < target) e = mid - 1;
                else if(nums.get(mid) > target) s = mid + 1;
                else return mid;
                
            }
        }
        
        return -1;
        
    } 
}