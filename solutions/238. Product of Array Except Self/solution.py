class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fromLeft = []
        ans = [1] * len(nums)
        leftProduct = 1
        for i in range(1, len(nums)):
            leftProduct *= nums[i - 1]
            ans[i] = leftProduct
        rightProduct = 1
        for i in range(len(nums) - 2, -1, -1):
            rightProduct *= nums[i + 1]
            ans[i] *= rightProduct
        return ans