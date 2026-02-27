// Last updated: 2/27/2026, 10:35:16 PM
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int max = 10000, min = -10000;
        int[] freq = new int[max - min + 1];

        for(int val : nums) freq[val - min]++;

        ArrayList<Integer>[] buckets = new ArrayList[nums.length + 1];

        for(int idx = 0; idx < buckets.length; idx++){
            buckets[idx] = new ArrayList<>();
        }

        for(int idx = 0; idx < freq.length; idx++){
            int val = idx + min;
            buckets[freq[idx]].add(val);
        }

        int[] res = new int[k];
        int b = 0;
        for(int idx = buckets.length - 1; idx > 0; idx--){
            for(int val : buckets[idx]){
                res[b++] = val;
                if(b == k) return res;
            }
        }
        return res;
    }
}