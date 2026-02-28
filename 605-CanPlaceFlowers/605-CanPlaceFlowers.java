// Last updated: 2/28/2026, 4:27:14 PM
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {

        if(n == 0) return true;

        if(flowerbed.length == 0) return false;
        if(flowerbed.length == 1 && flowerbed[0] == 0) return n <= 1;


        int i = 0, j = 1, k = 2;
        int count = 0;

        List<Integer> res = new ArrayList<>();

        for(int x = 0; x < flowerbed.length ; x++){
            res.add(flowerbed[x]);
        }     

        res.add(0,0);
        res.add(0);
      

        while(k < res.size()){
            if(res.get(i) == 0 && res.get(j) == 0 && res.get(k) == 0){
                res.set(j,1);
                count++;
            }

            i++;
            j++;
            k++;
        }


        

        return n <= count;
    }
}