// Last updated: 2/27/2026, 5:02:36 PM
class Solution {
    public int[] findEvenNumbers(int[] digits) {
    
        Set<Integer> result = new HashSet<>();
        
        Arrays.sort(digits);
        
        for(int i=0; i<digits.length; i++){
            if(digits[i]==0) continue;
            
        for(int j=0; j<digits.length; j++){
            if(j==i) continue;
        
            for(int k=0; k<digits.length;k++){
                if(k==i||k==j) continue;

                int digit= (digits[i]*100+digits[j]*10+digits[k]);
                    if(digit%2==0) result.add(digit);

            }
        }
    }
        

        
int []ans = new int[result.size()];

int index=0;
        
        for(int num : result)
            ans[index++] = num;
        


Arrays.sort(ans);

return ans;

}
}