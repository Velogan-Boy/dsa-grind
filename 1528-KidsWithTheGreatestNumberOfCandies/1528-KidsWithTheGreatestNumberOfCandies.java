// Last updated: 2/28/2026, 4:26:01 PM
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        
        ArrayList<Boolean> result = new ArrayList<>(candies.length);
        
        for(int i = 0; i < candies.length ; i++){
            if(candies[i] + extraCandies >= max(candies)){
                result.add(true);
            }else{
                result.add(false);
            }
        }
        
        
        return result;
        
}
    
    static int max(int[] arr){
        int max = arr[0];
        
        for(int i = 0; i < arr.length; i++){
            if(max < arr[i]) max = arr[i];
        }
        
        return max;
    }
}