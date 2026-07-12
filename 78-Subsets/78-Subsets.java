// Last updated: 7/12/2026, 6:24:01 PM
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<Integer> list = new ArrayList<Integer>();
        List<List<Integer>> res = new ArrayList<>();

        func(nums,0,list,res);

        return res;
    }

    public void func(int[] nums, int index,List<Integer> list, List<List<Integer>> res){

        if(index == nums.length){
            res.add(new ArrayList(list));
            return;
        }

        // pick
        list.add(nums[index]);
        func(nums,index + 1,list,res);

        // not pick
        list.remove(list.size() - 1);
        func(nums,index + 1,list,res);

    }
}