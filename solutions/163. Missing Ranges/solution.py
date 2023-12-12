class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        sol = []
        i = 0
        if lower not in nums:
            nums.insert(0, lower - 1)
        if upper not in nums:
            nums.append(upper + 1)
        while i < len(nums) - 1:
            if nums[i] + 1 != nums[i+1]:
                if nums[i] + 2 == nums[i+1]:
                    sol.append(str(nums[i] + 1))
                else:
                    sol.append("{}->{}".format(nums[i]+1, nums[i + 1]-1))
            i += 1
        return sol
