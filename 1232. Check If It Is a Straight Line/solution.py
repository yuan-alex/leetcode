class Solution:
    def slope(self, p1, p2):
        if p2[0] - p1[0] == 0:
            return None
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        startSlope = self.slope(coordinates[0], coordinates[1])
        for i in range(1, len(coordinates) - 1):
            if self.slope(coordinates[i], coordinates[i + 1]) != startSlope:
                return False
        return True