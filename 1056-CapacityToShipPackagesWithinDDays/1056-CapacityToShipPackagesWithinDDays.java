// Last updated: 2/28/2026, 4:26:18 PM
class Solution {
    public int shipWithinDays(int[] weights, int days) {        
        int len = weights.length;
        int maxWeights = 0;
        int max  = Integer.MIN_VALUE;
        for(int i = 0;i < len;i++) {
            max=Math.max(max,weights[i]);
           maxWeights += weights[i];
        }
        int start = max;
        int end = maxWeights;
           while(start <= end) {
               int midWeight = (start+end) / 2;
               if(isCap(weights,midWeight,days)) {
                 end = midWeight - 1;
               } else {
                    start = midWeight + 1;
               }
           }
           return start;
    }

    boolean isCap(int weights[],int weight,int days) {
int sum = 0;
int count = 0;
    for(int i = 0;i < weights.length;i++) {
                sum+=weights[i];
                if(sum > weight) {
                        count++;
                        sum=weights[i];
                }
    }
    if(sum <= weight) count++;
    if(count <= days)  return true;
     return false;    
    }
}
