// Last updated: 2/28/2026, 4:25:50 PM
class Solution {
public:
   vector<int> buildArray(vector<int>& nums) 
	{
		int n = nums.size();

		for(int i=0;i<n;i++)
		{
			nums[i] = nums[i] + n*(nums[nums[i]]%n);
		}

		for(int i=0;i<n;i++)
		{
			nums[i] = nums[i]/n;
		}
		return nums;
	}
};