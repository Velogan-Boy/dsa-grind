// Last updated: 7/12/2026, 6:25:51 PM


bool isPalindrome(int x){
    long num = x;
    long rev_num = 0;
    int dig;
    
    while(num != 0 && num>=0){
        dig = num % 10;
        num /= 10;
        rev_num = (rev_num * 10) + dig;
    }
    
    return rev_num==x;
}