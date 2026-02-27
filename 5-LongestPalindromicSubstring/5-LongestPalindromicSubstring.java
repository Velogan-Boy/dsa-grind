// Last updated: 2/27/2026, 5:12:17 PM
class Solution {
    public String longestPalindrome(String str) {

        if(str == null || str.length() < 1) return "";

        int start = 0;
		int end = 0;

		for(int i = 0; i < str.length() ; i++){

			int len1 = expandFromCenter(str,i - 1,i + 1);
			int len2 = expandFromCenter(str,i,i+1);

			int len = Math.max(len1,len2);

			if(len > end - start){
				start = i - ((len - 1 ) / 2);
				end = i + (len / 2);
			}

		}

		return str.substring(start,end + 1);
    }


	public  int expandFromCenter(String str, int left, int right){

        if(str == null || str.length() < 1) return 0;


		while(left >= 0 && right < str.length() && str.charAt(left) == str.charAt(right)){
			left--;
			right++;
		}

		return right - left - 1;


	}

}