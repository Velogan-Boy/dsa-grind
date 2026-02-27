// Last updated: 2/27/2026, 5:03:39 PM
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int rStart = 0;
        int rEnd = matrix.length - 1;
        
        int cStart = 0;
        int cEnd = matrix[0].length - 1;
        int cMid = cStart + (cEnd - cStart) / 2;
    
        // if element is not there
         if(target < matrix[0][0] || target > matrix[rEnd][cEnd])
            return false;
            
        // if there is only one row
        if(rStart == rEnd)
        return binarySearch(matrix,rStart, cStart,cEnd, target);
        
        // if there is only one column
        if(cStart == cEnd){
             while(rStart <= rEnd){
            int rMid = rStart + (rEnd - rStart) / 2;
            
            if(matrix[rMid][cStart] == target) 
                return true;
            if(matrix[rMid][cStart] > target)
                rEnd = rMid - 1;
            else
                rStart = rMid + 1;
        }
        
        return false;
        
        }
         
        while(rEnd - rStart > 1){
            int rMid = rStart + (rEnd - rStart) / 2;
            if(matrix[rMid][cMid] == target) 
                return true;
            if(matrix[rMid][cMid] > target) rEnd = rMid;
            else rStart = rMid;
        }
        
        if(matrix[rStart][cMid] <= target && matrix[rStart][cEnd] >= target)
            return binarySearch(matrix,rStart,cMid,cEnd,target);
        if(matrix[rStart][cMid] > target && matrix[rStart][cStart] <= target)
            return binarySearch(matrix,rStart,cStart,cMid,target);
            
        if(matrix[rEnd][cMid] <= target && matrix[rEnd][cEnd] >= target)
            return binarySearch(matrix,rEnd,cMid,cEnd,target);
        if(matrix[rEnd][cMid] > target && matrix[rEnd][cStart] <= target)
            return binarySearch(matrix,rEnd,cStart,cMid,target);
        
        return false;
    }
    
    public boolean binarySearch(int[][] matrix, int row, int cStart, int cEnd, int target){
        
        while(cStart <= cEnd){
            int cMid = cStart + (cEnd - cStart) / 2;
            
            if(matrix[row][cMid] == target) 
                return true;
            if(matrix[row][cMid] > target)
                cEnd = cMid - 1;
            else
                cStart = cMid + 1;
        }
        
        return false;
        
        
    }
}