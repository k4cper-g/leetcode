class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int number = nums[i];
            print(number)
            if(!map.containsKey(number)) {
                map.put(number, 1);
            } else {
                map.put(number, map.get(number) + 1);
            }
        }

        int[] topFrequent = new int[k];

        for(int j = 0; j < k; j++) {
            int maxKey = Collections.max(map.entrySet(), Map.Entry.comparingByValue()).getKey();
            topFrequent[j] = maxKey;
            map.remove(maxKey);
        }
        return topFrequent;
    }
}
