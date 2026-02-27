// Last updated: 2/27/2026, 5:02:59 PM
class Solution {
      public boolean validPalindrome(String s) {
    return helper(s, 0, s.length() - 1, true);
  }

  private boolean helper(String s, int l, int r, boolean okRemove) {
	//base case - pointer met, our string is a palindrome
    if (l >= r)
      return true;
	//check if chars are same - palindrome is possible, advancing to the center
    if (s.charAt(l) == s.charAt(r))
      return helper(s, l + 1, r - 1, okRemove);
    else
	  //if chars are different - skip one or another, set remove flag to false
      return okRemove && (helper(s, l + 1, r, false) || helper(s, l, r - 1, false));
  }
}