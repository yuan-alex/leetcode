# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        left, right = 0, binaryMatrix.dimensions()[1] - 1

        while left <= right:
            mid = (left + right) // 2
            pointers = {
                row: binaryMatrix.get(row, mid)
                for row in range(0, binaryMatrix.dimensions()[0])
            }
            pointers = {row: val for row, val in pointers.items() if val == 1}

            if len(pointers) == 0:
                left = mid + 1
                continue

            if mid == 0:
                return 0

            valid = True
            for row, val in pointers.items():
                if binaryMatrix.get(row, mid - 1) == 1:
                    right = mid - 1
                    valid = False

            if valid:
                return mid

        return -1