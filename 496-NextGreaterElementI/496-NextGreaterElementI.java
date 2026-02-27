// Last updated: 2/27/2026, 10:35:12 PM
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {

        HashMap<Integer,Integer> hm = new HashMap<>();

        for(int i = 0; i < nums1.length; i++){
            hm.put(nums1[i],i);
        }

        
        int[] res = new int[nums1.length];

        for(int i = 0; i < res.length; i++){
            res[i] = -1;
        }

       for(int i = 0; i < nums2.length; i++){
           if(hm.containsKey(nums2[i])){
               for(int x = i; x < nums2.length; x++){
                    if(nums2[x] > nums2[i]){
                        res[hm.get(nums2[i])] = nums2[x];
                        break;
                    }
               }
               
           }
       }

       return res;



    }
}