// Last updated: 2/28/2026, 4:25:58 PM
class Solution {
    public int numSubseq(int[] nums, int target) {
    Arrays.sort(nums);
    int l=0,r=nums.length,ans=0;
    int [] p =new int[r];
    p[0]=1;
    for(int i=1;i<r;i++)
        p[i] = (p[i-1] << 1)%1000000007;
    r--;
    while(l<=r){
        if(nums[l]+nums[r]<=target){
          ans+=p[r-l];
          ans%=1000000007;
          l++;
        }
        else
        r--;
    }
    return ans;
    }
}