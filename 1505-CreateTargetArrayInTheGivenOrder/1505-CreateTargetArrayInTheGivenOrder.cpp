// Last updated: 2/28/2026, 4:26:08 PM
class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
    vector<int> target;
    
    for(int i=0;i<index.size();++i) {
        target.insert(target.begin()+index[i],nums[i]);
    }
        
    return target;
    }
    
};