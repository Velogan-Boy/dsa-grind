// Last updated: 2/27/2026, 9:36:30 PM
class Solution {
    public int subtractProductAndSum(int n) {
        
        int num = n;
        int prod = 1;
        int sum = 0;
        
        
        while(num > 0){
            prod = prod * (num % 10);
            sum = sum + (num % 10);
            num /= 10;
        }
        
        return prod - sum;
        
    }
}