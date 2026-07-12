// Last updated: 7/12/2026, 6:25:43 PM
public class Solution {
public boolean isValid(String s) {
    char [] arr = s.toCharArray();
	Stack stack = new Stack();
	for(char ch : arr){
		if(stack.isEmpty()){
			stack.push(ch);
		}else{
			char top = (char)stack.lastElement();
			if(ch - top == 1 || ch - top == 2){
				stack.pop();
			}else{
				stack.push(ch);
			}
		}
	}
	if(stack.isEmpty()){
	    return true;
	}
	return false;
}
}