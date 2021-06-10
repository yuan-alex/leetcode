class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        ans = [0] * n
        # compare in reverse because the largest values will be on the most left or right of the array
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                ans[i] = nums[right] ** 2
                right -= 1
            else:
                ans[i] = nums[left] ** 2
                left += 1
        return ans