class Solution {
    public String longestCommonPrefix(String[] strs) {

        StringBuilder prefix = new StringBuilder();
        String first = strs[0];
        boolean flag = true;
        int count = 0;
        int i = 0;

        if(first.isEmpty()) {
            return first;
        }

        while(flag) {
            if(i >= first.length()) {
                break;
            }
            for(String s: strs) {
                if(s.length() == i) {
                    break;
                }
                if(first.charAt(i) == s.charAt(i)) {
                    count++;
                }
            }
            if(count != strs.length) {
                flag = false;
            } else {
                prefix.append(first.charAt(i));
            }
            count = 0;
            i++;
        }
        return prefix.toString();

    }
}
