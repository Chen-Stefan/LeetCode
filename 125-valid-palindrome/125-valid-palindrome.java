class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        int start = 0, end = s.length() - 1;
        
        while (start < end) {
            char char1 = s.charAt(start);
            if (!Character.isLetterOrDigit(char1)) {
                start++;
                continue;
            }
            char char2 = s.charAt(end);
            if (!Character.isLetterOrDigit(char2)) {
                end--;
                continue;
            }
            
            if (char1 == char2) {
                start ++;
                end --;
            } else {
                return false;
            }
        }
        
        return true;
    }
}