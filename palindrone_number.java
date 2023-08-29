// 9. Palindrone Number 

class Solution {
    public boolean isPalindrome(int x) {
        int val = x;
        int reversed = 0;
        while(val != 0) {
            reversed = reversed*10 + val%10;
            val = val/10;
        }
        if(x < 0 || x != reversed) {
            return false;
        } else {
            return true;
        }
    }
}
