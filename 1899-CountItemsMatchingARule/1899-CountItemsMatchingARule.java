// Last updated: 2/27/2026, 5:11:06 PM
class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        
        int index = 0;
        
        if(ruleKey.equals("color")) index = 1;
        else if(ruleKey.equals("name")) index = 2;
        
        int count = 0;
        
        for(List<String> item:items){
            if(item.get(index).equals(ruleValue)){
                count++;
            }
        }
        
        return count;
    }
}