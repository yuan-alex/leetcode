class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        solution = set()
        sequences = {}
        for i in range(len(s) - 9):
            print(i, i + 10)
            sequence = s[i:i + 10]
            if sequence in sequences:
                solution.add(sequence)
                sequences[sequence] += 1
            else:
                sequences[sequence] = 1
        return list(solution)
