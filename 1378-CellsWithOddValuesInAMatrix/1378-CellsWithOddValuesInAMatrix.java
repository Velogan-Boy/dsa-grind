// Last updated: 2/28/2026, 4:26:11 PM
class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        // Step 1: Accumulate row and column increments first
        int[] rows = new int[m];
        int[] cols = new int[n];
        for (int i = 0; i < indices.length; i++) {
            rows[indices[i][0]] += 1;
            cols[indices[i][1]] += 1;
        }

        /**
        * Step 2: Calculate the value of cell in m x n matrix
        * and increase the result counter if the value is an odd number
        */
        int result = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if ((rows[r] + cols[c]) % 2 != 0) {
                    result++;
                }
            }
        }
        
        return result;
    }
}