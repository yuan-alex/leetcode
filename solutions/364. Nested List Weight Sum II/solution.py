# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:
    def traverse(self, nestedList, integerCache, depth, depthCache):
        for i in nestedList:
            if i.isInteger():
                depthCache.append(depth)
                integerCache.append(i.getInteger())
            else:
                self.traverse(i.getList(), integerCache, depth + 1, depthCache)

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        integerCache = []
        depthCache = []
        self.traverse(nestedList, integerCache, 1, depthCache)
        if len(depthCache) == 0:
            return 0
        maxDepth = max(depthCache)
        return sum(
            [
                integerCache[i] * (maxDepth - depthCache[i] + 1)
                for i in range(0, len(integerCache))
            ]
        )
