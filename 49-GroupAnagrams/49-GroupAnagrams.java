// Last updated: 7/12/2026, 6:24:58 PM
class Solution {

    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            int count[] = new int[26];

            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }

            String countString = Arrays.toString(count);

            map.putIfAbsent(countString, new ArrayList<>());
            map.get(countString).add(s);
        }


         return new ArrayList<>(map.values());
        
    }
}
