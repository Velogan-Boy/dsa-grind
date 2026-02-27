// Last updated: 2/27/2026, 5:20:00 PM
class Solution {
    public int reverse(int x) {
                            
            int rev = 0;
            int signMultiplier = 1;
        
        if(x == 0) return 0;
            
            if(x < 0) {
                signMultiplier = -1;
                x = x * -1;
            }
       
            
            while(x > 0){
                 
           if (rev * signMultiplier > Integer.MAX_VALUE / 10 || rev * signMultiplier < Integer.MIN_VALUE / 10) {
                return 0;
            }
                
                rev = rev * 10 + (x % 10);
                x /= 10;
            }
            
                      
            return (rev * signMultiplier);

            
            
       
        
        
    }
}