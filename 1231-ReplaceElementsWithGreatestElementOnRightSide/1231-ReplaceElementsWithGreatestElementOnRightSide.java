// Last updated: 2/28/2026, 4:26:13 PM
class Solution {
       public int[] replaceElements(int[] A) {
        for (int i = A.length - 1, mx = -1; i >= 0; --i)
            mx = Math.max(A[i], A[i] = mx);
        return A;
    }
}