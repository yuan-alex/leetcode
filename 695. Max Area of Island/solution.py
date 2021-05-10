class Solution:
    def traverse(self, grid, y, x):
        grid[y][x] = 0
        area = 0
        
        # up
        if y - 1 >= 0 and grid[y - 1][x] == 1:
            area += self.traverse(grid, y - 1, x)
        
        # right
        if x + 1 < len(grid[0]) and grid[y][x + 1] == 1:
            area += self.traverse(grid, y, x + 1)
        
        # down
        if y + 1 < len(grid) and grid[y + 1][x] == 1:
            area += self.traverse(grid, y + 1, x)
        
        # left
        if x - 1 >= 0 and grid[y][x - 1] == 1:
            area += self.traverse(grid, y, x - 1)
            
        return area + 1
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSoFar = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if grid[y][x] == 1:
                    area = self.traverse(grid, y, x)
                    if area > maxSoFar:
                        maxSoFar = area
        return maxSoFar