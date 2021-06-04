class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p2 = 0
        for p1 in range(0, len(nums)):
            if nums[p1] != val:
                nums[p2] = nums[p1]
                p2 += 1
        return p2