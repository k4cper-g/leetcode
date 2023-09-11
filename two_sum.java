import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int one = 0;
        int two = 0;
        for(int i = 0; i < nums.length; i++) {
            for(int j = 0; j < nums.length; j++) {
                if(nums[i] + nums[j] == target && i != j) {
                    one = i;
                    two = j;
                }
            }
        }
        int[] arr = {one,two};
        Arrays.sort(arr);
        return arr;
    }
}
