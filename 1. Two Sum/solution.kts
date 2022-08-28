class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        var ans = IntArray(2);
        var history = IntArray(nums.size);
        for (i in nums.indices) {
            var x = target - nums[i];
            for (j in history.indices) {
                if (history[j] == x && i != j) {
                    ans.set(0, i);
                    ans.set(1, j);
                }
            }
            history.set(i, nums[i]);
        }
        return ans;
    }
}
