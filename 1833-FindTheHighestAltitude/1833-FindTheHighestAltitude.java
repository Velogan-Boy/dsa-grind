// Last updated: 2/27/2026, 5:02:39 PM
class Solution {
    public int largestAltitude(int[] gain) {
        int[] altitudes = new int[gain.length + 1];
        
        altitudes[0] = 0;
        
        for(int i = 1; i < altitudes.length ; i++){
            altitudes[i] = altitudes[i - 1] + gain[i-1]; 
        }
        
        return max(altitudes);
    }
    
    static int max(int[] arr){
        int max = arr[0];
        
        for(int i=0; i < arr.length; i++){
            if(max < arr[i]) max = arr[i];
        }
        
        return max;
    }
}