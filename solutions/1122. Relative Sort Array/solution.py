class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1Count = collections.Counter(arr1)
        arr2Count = collections.Counter(arr2)
        ans = []
        for i in arr2Count:
            ans += [i] * arr1Count[i]
            arr1Count.pop(i)
        for i in sorted(list(arr1Count.keys())):
            ans += [i] * arr1Count[i]
        return ans