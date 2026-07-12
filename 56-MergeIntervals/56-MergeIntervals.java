// Last updated: 7/12/2026, 6:24:36 PM
class Solution {
    public int[][] merge(int[][] intervals) {

        Arrays.sort(intervals,(i1,i2) -> Integer.compare(i1[0],i2[0]));

        ArrayList<int[]> output = new ArrayList<>();

        int start = intervals[0][0];
        int end = intervals[0][1];

        for(int i = 1; i < intervals.length; i++){
            int s = intervals[i][0];
            int e = intervals[i][1];

            if(s <= end){
                end = Math.max(end,e);
            }else{
                output.add(new int[] {start,end});
                start = s;
                end = e;
            }
        }

        output.add(new int[]{start,end});

         return output.toArray(new int[output.size()][2]); 
        
    }
}