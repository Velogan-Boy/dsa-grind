// Last updated: 2/27/2026, 9:36:45 PM
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        
        int start = 0;
        int n = letters.length;
        int end = n - 1;
        int mid;

        while(start <= end){
            mid = start + (end-start)/2;

            if(letters[mid] <= target) start = mid + 1;
            else end = mid - 1;
        }

        return letters[start % n];


    }
}