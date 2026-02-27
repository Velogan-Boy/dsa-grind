// Last updated: 2/27/2026, 5:11:12 PM
class Solution {
    public boolean canReach(int[] arr, int start) {
	
        if(start<0 || start>=arr.length || arr[start]<0) return false;   // terminating conditions
        
        if(arr[start]==0){   //reached the target
            return true;
        }
        
        arr[start] = -arr[start];
        
        return canReach(arr,start+arr[start])||canReach(arr,start-arr[start]);   //checking in both direction
    }
}