// Last updated: 2/27/2026, 5:22:03 PM
class Solution {
    public boolean isIsomorphic(String s, String t) {

        if(s.length() != t.length()) return false;

        HashMap<Character,Character> hm1 = new HashMap<>();
        HashMap<Character,Character> hm2 = new HashMap<>();


        for(int i = 0; i < s.length(); i++){
            Character x = s.charAt(i);
            Character y = t.charAt(i);

            if(hm1.containsKey(x) && hm1.get(x) != y) return false;
            if(hm2.containsKey(y) && hm2.get(y) != x) return false;


            hm1.put(x,y);
            hm2.put(y,x);
        }

        return true;
        
    }
}