// Last updated: 2/27/2026, 5:22:34 PM
class Solution {
	public static int search(int[] nums, int target) {
        int pivotIndex = findPivot(nums);
        int ans;
                
        if(pivotIndex == -1){
            ans = binarySearch(nums,target,0,nums.length - 1);
            return ans;
        }
        
        if(nums[pivotIndex] == target) return pivotIndex;
        
        ans = binarySearch(nums,target,0,pivotIndex - 1);
        
        if(ans == -1){
            ans = binarySearch(nums,target,pivotIndex + 1, nums.length - 1);
            return ans;
        }
        
        return ans;
        
        
        
        
        
    }
    
    static int findPivot(int[] num) {
    
    if(num.length == 0 || num.length == 1) return -1;
    
    int s = 0;
    int e = num.length - 1;
        

    while (s <= e) {
      int mid = s + (e - s) / 2;

      if (mid < e && num[mid] > num[mid + 1])
        return mid;
      else if (mid > s && num[mid] < num[mid - 1])
        return mid - 1;
      else if (num[mid] <= num[s])
        e = mid - 1;
      else if ( num[mid] > num[s])
        s = mid + 1;

    }

    return -1;

  }

  static int binarySearch(int[] num, int target, int s, int e) {

    while (s <= e) {
            int mid = s + (e - s) / 2;

      if (num[mid] == target)
        return mid;
      else if (num[mid] < target)
        s = mid + 1;
      else
        e = mid - 1;
    }

    return -1;

  }

}