// Last updated: 2/27/2026, 5:11:25 PM
class Solution {
    public int calPoints(String[] operations) {
        
        if(operations.length == 0) return 0;

        Stack<String> st  = new Stack<>();

        for(int i = 0; i < operations.length; i++){
            String curr = operations[i];

            if(curr.equals("C")) st.pop();
            else if(curr.equals("+")){
                Integer a = Integer.parseInt(st.pop());
                Integer b =  Integer.parseInt(st.pop());
                st.push(b.toString());
                st.push(a.toString());
                Integer c = a + b;
                st.push(c.toString());
            }
            else if(curr.equals("D")) st.push(Integer.parseInt(st.peek()) * 2 + "");
            else st.push(curr);
            
        }

        int sum = 0;
        while(!st.isEmpty()) sum += Integer.parseInt(st.pop());

        return sum;
        
    }
}