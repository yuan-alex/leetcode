class Solution:
    def traverse(self, grid, y, x):
        grid[y][x] = "0"
        if y - 1 >= 0 and grid[y - 1][x] == "1":
            self.traverse(grid, y - 1, x)
        if x + 1 < len(grid[0]) and grid[y][x + 1] == "1":
            self.traverse(grid, y, x + 1)
        if y + 1 < len(grid) and grid[y + 1][x] == "1":
            self.traverse(grid, y + 1, x)
        if x - 1 >= 0 and grid[y][x - 1] == "1":
            self.traverse(grid, y, x - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] == "1":
                    self.traverse(grid, y, x)
                    count += 1
        return count