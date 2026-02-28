// Last updated: 2/28/2026, 4:27:37 PM
/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        long low = 1;
        long high = (long) n;
        
        while(low <= high){
            long mid = (low + high) / 2;
            if(isBadVersion((int) mid)) high = mid - 1;
            else low = mid + 1;
        }
        
        return (int) low;
        
        
    }
}