// Last updated: 2/28/2026, 4:25:56 PM
class Solution {
    public int diagonalSum(int[][] mat) {
        int sum =0;
        for(int i=0;i<mat.length;i++){
		// primary diagonal element - added
            sum+=mat[i][i];
		// secondary diagonal element - added
            sum+=mat[0+i][mat.length-1-i];
        }
        // if our matrix is of odd length then only we will have an overlapping element between the two diagonals
        if(mat.length%2!=0){
            
            sum-=mat[mat.length/2][mat.length/2];
        }
        return sum;
    }
}