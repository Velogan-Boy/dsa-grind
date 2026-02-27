// Last updated: 2/27/2026, 5:11:13 PM
class Solution {
    public int findNumbers(int[] nums) {
        
        int evenDigitNumbers = 0;
        
        for(int num : nums){
            if(checkEvenDigits(num) == 0){
                evenDigitNumbers++;
            }
        }
        
        return evenDigitNumbers;
        
        
        
    }
    
    static int checkEvenDigits(int num){
        int count = 0;
        
        while(num > 0){
            count++;
            num /= 10;
        }
        
        return count % 2;
    }
}