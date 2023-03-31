class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1, 1]
        for i in range(1, rowIndex):
            new_row = [1]
            for j in range(0, len(row) - 1):
                new_row.append(row[j] + row[j + 1])
            new_row.append(1)
            row = new_row
        return row
