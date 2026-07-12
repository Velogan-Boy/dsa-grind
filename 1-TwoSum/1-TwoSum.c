// Last updated: 7/12/2026, 6:26:18 PM


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

 

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    
    *returnSize = 2;
        
    int i, j;
    int flag = 0;
    
    int *soln;
    
    soln = (int*) malloc(2*sizeof(int));
    
    for( i = 0 ; i < numsSize ; i++){
       for(j = i + 1; j < numsSize ; j++){
           if(nums[i] + nums[j] == target){
               soln[0] = i;
               soln[1] = j;
               flag = 1;
               break;
           }
       }
   }
    
    if(flag == 1){
        return soln;
    }
    
    return NULL;
    
    
    

}