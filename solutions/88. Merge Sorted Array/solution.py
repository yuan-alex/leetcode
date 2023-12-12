class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new = []
        index1 = 0
        index2 = 0
        while index1 < m or index2 < n:
            if index1 >= m:
                new.append(nums2[index2])
                index2 += 1
            elif index2 >= n:
                new.append(nums1[index1])
                index1 += 1
            elif nums1[index1] == nums2[index2]:
                new.append(nums1[index1])
                new.append(nums2[index2])
                index1 += 1
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                new.append(nums1[index1])
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                new.append(nums2[index2])
                index2 += 1
        nums1[:] = new[:]