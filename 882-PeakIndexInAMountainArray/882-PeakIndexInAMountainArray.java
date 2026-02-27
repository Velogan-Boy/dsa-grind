// Last updated: 2/27/2026, 5:21:40 PM
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        
        int s = 0;
        int e = arr.length - 1;
        
        while(s < e){
            int mid = s + (e - s) / 2;
            
            if(arr[mid] > arr[mid + 1]){
                // we are in decreasing part of the array
                e = mid;
            } else if(arr[mid] < arr[mid + 1]){
                s = mid + 1;
            } 
        }
        
        return s;
        
        
    }
}