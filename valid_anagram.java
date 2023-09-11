import java.util.*;

class Solution {
    public boolean isAnagram(String s, String t) {
        List<String> slist = new ArrayList<>(Arrays.asList(s.split("")));
        List<String> tlist = new ArrayList<>(Arrays.asList(t.split("")));
        Collections.sort(slist);
        Collections.sort(tlist);
        return slist.equals(tlist);
    }
}
