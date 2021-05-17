# Really bad solution, should probably fix up later
class Solution:
    def binarySearch(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if numbers[mid] == target:
                return mid
            if numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            attempt = self.binarySearch(numbers, target - num)
            if attempt != -1 and attempt != i:
                ans = [i + 1, attempt + 1]
                ans.sort()
                return ans